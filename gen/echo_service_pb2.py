# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='echo_service.proto',
  package='echo',
  syntax='proto3',
  serialized_pb=_b('\n\x12\x65\x63ho_service.proto\x12\x04\x65\x63ho\x1a\x1cgoogle/api/annotations.proto\"\x1e\n\rStringMessage\x12\r\n\x05value\x18\x01 \x01(\t2h\n\x0bYourService\x12Y\n\x04\x45\x63ho\x12\x13.echo.StringMessage\x1a\x13.echo.StringMessage\"\'\x82\xd3\xe4\x93\x02!\"\x08/v1/echo:\x01*Z\x12\x12\x10/v1/echo/{value}b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STRINGMESSAGE = _descriptor.Descriptor(
  name='StringMessage',
  full_name='echo.StringMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='echo.StringMessage.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['StringMessage'] = _STRINGMESSAGE

StringMessage = _reflection.GeneratedProtocolMessageType('StringMessage', (_message.Message,), dict(
  DESCRIPTOR = _STRINGMESSAGE,
  __module__ = 'echo_service_pb2'
  # @@protoc_insertion_point(class_scope:echo.StringMessage)
  ))
_sym_db.RegisterMessage(StringMessage)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class YourServiceStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Echo = channel.unary_unary(
          '/echo.YourService/Echo',
          request_serializer=StringMessage.SerializeToString,
          response_deserializer=StringMessage.FromString,
          )


  class YourServiceServicer(object):

    def Echo(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_YourServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Echo': grpc.unary_unary_rpc_method_handler(
            servicer.Echo,
            request_deserializer=StringMessage.FromString,
            response_serializer=StringMessage.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'echo.YourService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaYourServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Echo(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaYourServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Echo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Echo.future = None


  def beta_create_YourService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('echo.YourService', 'Echo'): StringMessage.FromString,
    }
    response_serializers = {
      ('echo.YourService', 'Echo'): StringMessage.SerializeToString,
    }
    method_implementations = {
      ('echo.YourService', 'Echo'): face_utilities.unary_unary_inline(servicer.Echo),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_YourService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('echo.YourService', 'Echo'): StringMessage.SerializeToString,
    }
    response_deserializers = {
      ('echo.YourService', 'Echo'): StringMessage.FromString,
    }
    cardinalities = {
      'Echo': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'echo.YourService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
