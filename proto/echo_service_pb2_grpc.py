# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto.echo_service_pb2 as proto_dot_echo__service__pb2


class EchoServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Echo = channel.unary_unary(
        '/echo.EchoService/Echo',
        request_serializer=proto_dot_echo__service__pb2.StringMessage.SerializeToString,
        response_deserializer=proto_dot_echo__service__pb2.StringMessage.FromString,
        )


class EchoServiceServicer(object):

  def Echo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EchoServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Echo': grpc.unary_unary_rpc_method_handler(
          servicer.Echo,
          request_deserializer=proto_dot_echo__service__pb2.StringMessage.FromString,
          response_serializer=proto_dot_echo__service__pb2.StringMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'echo.EchoService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))