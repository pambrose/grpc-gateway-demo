GOSRC = ${GOPATH}/src
GOOGLEAPIS = ${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis/
PBAPIS = ${HOME}/git/protobuf/src

.PHONY: swagger

default: all

all: go-stubs py-stubs go-proxy swagger

go-stubs:
	protoc -I/usr/local/include -I. -I${GOSRC} -I${GOOGLEAPIS} --go_out=,plugins=grpc:. ./pb/echo_service.proto

go-proxy:
	protoc -I/usr/local/include -I. -I${GOSRC} -I${GOOGLEAPIS} --grpc-gateway_out=logtostderr=true:. ./pb/echo_service.proto

py-stubs:
	python -m grpc_tools.protoc -I. -I${GOOGLEAPIS} -I${PBAPIS} --python_out=. --grpc_python_out=. ./pb/echo_service.proto

swagger:
	cd pb; protoc -I/usr/local/include -I. -I${GOSRC} -I${GOOGLEAPIS} --swagger_out=logtostderr=true:../swagger ./echo_service.proto

