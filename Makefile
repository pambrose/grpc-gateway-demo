go-stubs:
	protoc -I/usr/local/include -I. -I${GOPATH}/src -I${GOPATH}/src/github.com/googleapis/googleapis/ --go_out=,plugins=grpc:./echo ./echo_service.proto

py-stubs:
	python -m grpc_tools.protoc -I. -I${GOPATH}/src/github.com/googleapis/googleapis -I${HOME}/git/protobuf/src --python_out=./gen --grpc_python_out=./gen ./echo_service.proto

proxy:
	protoc -I/usr/local/include -I. -I${GOPATH}/src -I${GOPATH}/src/github.com/googleapis/googleapis/ --grpc-gateway_out=logtostderr=true:./echo ./echo_service.proto

swag:
	protoc -I/usr/local/include -I. -I${GOPATH}/src -I${GOPATH}/src/github.com/googleapis/googleapis/ --swagger_out=logtostderr=true:./swagger ./echo_service.proto

all: go-stubs py-stubs proxy swag
