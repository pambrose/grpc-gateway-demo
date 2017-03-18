#!/usr/bin/env python2

from grpc.tools import protoc

protoc.main(
    (
        '',
        '-I.',
        '-I/Users/pambrose/go/src/github.com/googleapis/googleapis',
        '-I/Users/pambrose/git/protobuf/src',
        '--python_out=./gen',
        '--grpc_python_out=./gen',
        './echo_service.proto',
    )
)
