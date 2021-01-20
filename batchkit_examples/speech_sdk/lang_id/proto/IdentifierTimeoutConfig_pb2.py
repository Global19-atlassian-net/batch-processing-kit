# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IdentifierTimeoutConfig.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='IdentifierTimeoutConfig.proto',
  package='skyman.languageId.rpc.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1dIdentifierTimeoutConfig.proto\x12\x18skyman.languageId.rpc.v1\"[\n\x17IdentifierTimeoutConfig\x12 \n\x18start_silence_timeout_ms\x18\x01 \x01(\r\x12\x1e\n\x16\x65nd_silence_timeout_ms\x18\x02 \x01(\rb\x06proto3'
)




_IDENTIFIERTIMEOUTCONFIG = _descriptor.Descriptor(
  name='IdentifierTimeoutConfig',
  full_name='skyman.languageId.rpc.v1.IdentifierTimeoutConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_silence_timeout_ms', full_name='skyman.languageId.rpc.v1.IdentifierTimeoutConfig.start_silence_timeout_ms', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_silence_timeout_ms', full_name='skyman.languageId.rpc.v1.IdentifierTimeoutConfig.end_silence_timeout_ms', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['IdentifierTimeoutConfig'] = _IDENTIFIERTIMEOUTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IdentifierTimeoutConfig = _reflection.GeneratedProtocolMessageType('IdentifierTimeoutConfig', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIERTIMEOUTCONFIG,
  '__module__' : 'IdentifierTimeoutConfig_pb2'
  # @@protoc_insertion_point(class_scope:skyman.languageId.rpc.v1.IdentifierTimeoutConfig)
  })
_sym_db.RegisterMessage(IdentifierTimeoutConfig)


# @@protoc_insertion_point(module_scope)
