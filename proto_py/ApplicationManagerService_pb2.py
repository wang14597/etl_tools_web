# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ApplicationManagerService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from proto_py import Task_pb2 as Task__pb2
from proto_py import CoordinatorJob_pb2 as CoordinatorJob__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ApplicationManagerService.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n7com.com.thoughtworks.bigdata.dataworkflow.proto.service',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x41pplicationManagerService.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\nTask.proto\x1a\x14\x43oordinatorJob.proto\" \n\x08JobStage\x12\x14\n\x05tasks\x18\x01 \x03(\x0b\x32\x05.Task\"4\n\x17GetDependenciesResponse\x12\x19\n\x06stages\x18\x01 \x03(\x0b\x32\t.JobStage\"7\n\x16GetDependenciesRequest\x12\r\n\x05jobId\x18\x01 \x01(\x05\x12\x0e\n\x06taskId\x18\x02 \x01(\t\" \n\x0fGetJobsResponse\x12\r\n\x05jobId\x18\x01 \x03(\x05\x32\xb2\x03\n\x19\x41pplicationManagerService\x12\x38\n\x06getJob\x12\x1b.google.protobuf.Int32Value\x1a\x0f.CoordinatorJob\"\x00\x12\x41\n\x08startJob\x12\x1b.google.protobuf.Int32Value\x1a\x16.google.protobuf.Empty\"\x00\x12\x38\n\x0bregisterJob\x12\x0f.CoordinatorJob\x1a\x16.google.protobuf.Empty\"\x00\x12*\n\x07getTask\x12\x16.google.protobuf.Empty\x1a\x05.Task\"\x00\x12\x33\n\x10updateTaskStatus\x12\x05.Task\x1a\x16.google.protobuf.Empty\"\x00\x12\x35\n\x07getJobs\x12\x16.google.protobuf.Empty\x1a\x10.GetJobsResponse\"\x00\x12\x46\n\x0fgetDependencies\x12\x17.GetDependenciesRequest\x1a\x18.GetDependenciesResponse\"\x00\x42\x39\n7com.com.thoughtworks.bigdata.dataworkflow.proto.serviceb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,Task__pb2.DESCRIPTOR,CoordinatorJob__pb2.DESCRIPTOR,])




_JOBSTAGE = _descriptor.Descriptor(
  name='JobStage',
  full_name='JobStage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='JobStage.tasks', index=0,
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
  serialized_start=130,
  serialized_end=162,
)


_GETDEPENDENCIESRESPONSE = _descriptor.Descriptor(
  name='GetDependenciesResponse',
  full_name='GetDependenciesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stages', full_name='GetDependenciesResponse.stages', index=0,
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
  serialized_start=164,
  serialized_end=216,
)


_GETDEPENDENCIESREQUEST = _descriptor.Descriptor(
  name='GetDependenciesRequest',
  full_name='GetDependenciesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='GetDependenciesRequest.jobId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='taskId', full_name='GetDependenciesRequest.taskId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=218,
  serialized_end=273,
)


_GETJOBSRESPONSE = _descriptor.Descriptor(
  name='GetJobsResponse',
  full_name='GetJobsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='GetJobsResponse.jobId', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=275,
  serialized_end=307,
)

_JOBSTAGE.fields_by_name['tasks'].message_type = Task__pb2._TASK
_GETDEPENDENCIESRESPONSE.fields_by_name['stages'].message_type = _JOBSTAGE
DESCRIPTOR.message_types_by_name['JobStage'] = _JOBSTAGE
DESCRIPTOR.message_types_by_name['GetDependenciesResponse'] = _GETDEPENDENCIESRESPONSE
DESCRIPTOR.message_types_by_name['GetDependenciesRequest'] = _GETDEPENDENCIESREQUEST
DESCRIPTOR.message_types_by_name['GetJobsResponse'] = _GETJOBSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobStage = _reflection.GeneratedProtocolMessageType('JobStage', (_message.Message,), {
  'DESCRIPTOR' : _JOBSTAGE,
  '__module__' : 'ApplicationManagerService_pb2'
  # @@protoc_insertion_point(class_scope:JobStage)
  })
_sym_db.RegisterMessage(JobStage)

GetDependenciesResponse = _reflection.GeneratedProtocolMessageType('GetDependenciesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDEPENDENCIESRESPONSE,
  '__module__' : 'ApplicationManagerService_pb2'
  # @@protoc_insertion_point(class_scope:GetDependenciesResponse)
  })
_sym_db.RegisterMessage(GetDependenciesResponse)

GetDependenciesRequest = _reflection.GeneratedProtocolMessageType('GetDependenciesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDEPENDENCIESREQUEST,
  '__module__' : 'ApplicationManagerService_pb2'
  # @@protoc_insertion_point(class_scope:GetDependenciesRequest)
  })
_sym_db.RegisterMessage(GetDependenciesRequest)

GetJobsResponse = _reflection.GeneratedProtocolMessageType('GetJobsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBSRESPONSE,
  '__module__' : 'ApplicationManagerService_pb2'
  # @@protoc_insertion_point(class_scope:GetJobsResponse)
  })
_sym_db.RegisterMessage(GetJobsResponse)


DESCRIPTOR._options = None

_APPLICATIONMANAGERSERVICE = _descriptor.ServiceDescriptor(
  name='ApplicationManagerService',
  full_name='ApplicationManagerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=310,
  serialized_end=744,
  methods=[
  _descriptor.MethodDescriptor(
    name='getJob',
    full_name='ApplicationManagerService.getJob',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._INT32VALUE,
    output_type=CoordinatorJob__pb2._COORDINATORJOB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='startJob',
    full_name='ApplicationManagerService.startJob',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._INT32VALUE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='registerJob',
    full_name='ApplicationManagerService.registerJob',
    index=2,
    containing_service=None,
    input_type=CoordinatorJob__pb2._COORDINATORJOB,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getTask',
    full_name='ApplicationManagerService.getTask',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=Task__pb2._TASK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='updateTaskStatus',
    full_name='ApplicationManagerService.updateTaskStatus',
    index=4,
    containing_service=None,
    input_type=Task__pb2._TASK,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getJobs',
    full_name='ApplicationManagerService.getJobs',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_GETJOBSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getDependencies',
    full_name='ApplicationManagerService.getDependencies',
    index=6,
    containing_service=None,
    input_type=_GETDEPENDENCIESREQUEST,
    output_type=_GETDEPENDENCIESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_APPLICATIONMANAGERSERVICE)

DESCRIPTOR.services_by_name['ApplicationManagerService'] = _APPLICATIONMANAGERSERVICE

# @@protoc_insertion_point(module_scope)
