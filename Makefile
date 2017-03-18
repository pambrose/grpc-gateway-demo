stubs:
	protoc -I/usr/local/include -I. -I${GOPATH}/src -I${GOPATH}/src/github.com/googleapis/googleapis/ --go_out=,plugins=grpc:./echo ./echo_service.proto

proxy:
	protoc -I/usr/local/include -I. -I${GOPATH}/src -I${GOPATH}/src/github.com/googleapis/googleapis/ --grpc-gateway_out=logtostderr=true:./echo ./echo_service.proto

swag:
	protoc -I/usr/local/include -I. -I${GOPATH}/src -I${GOPATH}/src/github.com/googleapis/googleapis/ --swagger_out=logtostderr=true:./swagger ./echo_service.proto

all: stubs proxy swag
