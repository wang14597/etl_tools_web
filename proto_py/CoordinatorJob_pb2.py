# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CoordinatorJob.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto_py import Task_pb2 as Task__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='CoordinatorJob.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n5com.com.thoughtworks.bigdata.dataworkflow.proto.model',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x43oordinatorJob.proto\x1a\nTask.proto\"\"\n\nNestedTask\x12\x14\n\x05tasks\x18\x01 \x03(\x0b\x32\x05.Task\"^\n\x0e\x43oordinatorJob\x12\r\n\x05jobId\x18\x01 \x01(\x05\x12\x14\n\x0cremainingJob\x18\x02 \x01(\x05\x12\x11\n\tjobStatus\x18\x03 \x01(\t\x12\x14\n\x05tasks\x18\x04 \x03(\x0b\x32\x05.TaskB7\n5com.com.thoughtworks.bigdata.dataworkflow.proto.modelb\x06proto3'
  ,
  dependencies=[Task__pb2.DESCRIPTOR,])




_NESTEDTASK = _descriptor.Descriptor(
  name='NestedTask',
  full_name='NestedTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='NestedTask.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=36,
  serialized_end=70,
)


_COORDINATORJOB = _descriptor.Descriptor(
  name='CoordinatorJob',
  full_name='CoordinatorJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='CoordinatorJob.jobId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remainingJob', full_name='CoordinatorJob.remainingJob', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jobStatus', full_name='CoordinatorJob.jobStatus', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='CoordinatorJob.tasks', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=72,
  serialized_end=166,
)

_NESTEDTASK.fields_by_name['tasks'].message_type = Task__pb2._TASK
_COORDINATORJOB.fields_by_name['tasks'].message_type = Task__pb2._TASK
DESCRIPTOR.message_types_by_name['NestedTask'] = _NESTEDTASK
DESCRIPTOR.message_types_by_name['CoordinatorJob'] = _COORDINATORJOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NestedTask = _reflection.GeneratedProtocolMessageType('NestedTask', (_message.Message,), {
  'DESCRIPTOR' : _NESTEDTASK,
  '__module__' : 'CoordinatorJob_pb2'
  # @@protoc_insertion_point(class_scope:NestedTask)
  })
_sym_db.RegisterMessage(NestedTask)

CoordinatorJob = _reflection.GeneratedProtocolMessageType('CoordinatorJob', (_message.Message,), {
  'DESCRIPTOR' : _COORDINATORJOB,
  '__module__' : 'CoordinatorJob_pb2'
  # @@protoc_insertion_point(class_scope:CoordinatorJob)
  })
_sym_db.RegisterMessage(CoordinatorJob)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
