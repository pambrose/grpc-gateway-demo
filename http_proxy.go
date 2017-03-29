package main

import (
    "flag"
    "net/http"

    "github.com/golang/glog"
    "golang.org/x/net/context"
    "github.com/grpc-ecosystem/grpc-gateway/runtime"
    "google.golang.org/grpc"

    pb "./proto"
    "strings"
    "path"
)

var (
    echoEndpoint = flag.String("echo_endpoint", "localhost:50051", "endpoint of YourService")
    swaggerDir = flag.String("swagger_dir", "swagger", "path to the directory which contains swagger definitions")
)

// allowCORS allows Cross Origin Resoruce Sharing from any origin.
// Don't do this without consideration in production systems.
func allowCORS(h http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        if origin := r.Header.Get("Origin"); origin != "" {
            w.Header().Set("Access-Control-Allow-Origin", origin)
            if r.Method == "OPTIONS" && r.Header.Get("Access-Control-Request-Method") != "" {
                preflightHandler(w, r)
                return
            }
        }
        h.ServeHTTP(w, r)
    })
}

func preflightHandler(w http.ResponseWriter, r *http.Request) {
    headers := []string{"Content-Type", "Accept"}
    w.Header().Set("Access-Control-Allow-Headers", strings.Join(headers, ","))
    methods := []string{"GET", "HEAD", "POST", "PUT", "DELETE"}
    w.Header().Set("Access-Control-Allow-Methods", strings.Join(methods, ","))
    glog.Infof("preflight request for %s", r.URL.Path)
    return
}

func serveSwagger(w http.ResponseWriter, r *http.Request) {
    if !strings.HasSuffix(r.URL.Path, ".swagger.json") {
        glog.Errorf("Not Found: %s", r.URL.Path)
        http.NotFound(w, r)
        return
    }

    glog.Infof("Serving %s", r.URL.Path)
    p := strings.TrimPrefix(r.URL.Path, "/" + *swaggerDir + "/")
    p = path.Join(*swaggerDir, p)
    http.ServeFile(w, r, p)
}

// newGateway returns a new gateway server which translates HTTP into gRPC.
func newGateway(ctx context.Context, opts ...runtime.ServeMuxOption) (http.Handler, error) {
    mux := runtime.NewServeMux(opts...)
    dialOpts := []grpc.DialOption{grpc.WithInsecure()}
    err := pb.RegisterEchoServiceHandlerFromEndpoint(ctx, mux, *echoEndpoint, dialOpts)
    if err != nil {
        return nil, err
    }
    return mux, nil
}

func Run(address string, opts ...runtime.ServeMuxOption) error {
    ctx := context.Background()
    ctx, cancel := context.WithCancel(ctx)
    defer cancel()

    sdir := "/" + *swaggerDir + "/"
    glog.Infof("Swagger files served from http://%s%s", address, sdir)

    mux := http.NewServeMux()
    mux.HandleFunc(sdir, serveSwagger)

    gw, err := newGateway(ctx, opts...)
    if err != nil {
        return err
    }
    mux.Handle("/", gw)

    glog.Infof("Listening on %s", address)
    return http.ListenAndServe(address, allowCORS(mux))
}

func main() {
    flag.Parse()
    defer glog.Flush()

    glog.Info("Starting http_proxy")

    if err := Run(":8080"); err != nil {
        glog.Fatal(err)
    }
}

