# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dgp/proto/annotations.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dgp.proto import geometry_pb2 as dgp_dot_proto_dot_geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dgp/proto/annotations.proto',
  package='dgp.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x64gp/proto/annotations.proto\x12\tdgp.proto\x1a\x18\x64gp/proto/geometry.proto\";\n\rBoundingBox2D\x12\t\n\x01x\x18\x01 \x01(\r\x12\t\n\x01y\x18\x02 \x01(\r\x12\t\n\x01w\x18\x03 \x01(\r\x12\t\n\x01h\x18\x04 \x01(\r\"\x81\x02\n\x17\x42oundingBox2DAnnotation\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\r\x12%\n\x03\x62ox\x18\x02 \x01(\x0b\x32\x18.dgp.proto.BoundingBox2D\x12\x0c\n\x04\x61rea\x18\x03 \x01(\r\x12\x0f\n\x07iscrowd\x18\x04 \x01(\x08\x12\x13\n\x0binstance_id\x18\x05 \x01(\r\x12\x46\n\nattributes\x18\x06 \x03(\x0b\x32\x32.dgp.proto.BoundingBox2DAnnotation.AttributesEntry\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x84\x01\n\rBoundingBox3D\x12\x1d\n\x04pose\x18\x01 \x01(\x0b\x32\x0f.dgp.proto.Pose\x12\r\n\x05width\x18\x02 \x01(\x01\x12\x0e\n\x06length\x18\x03 \x01(\x01\x12\x0e\n\x06height\x18\x04 \x01(\x01\x12\x11\n\tocclusion\x18\x05 \x01(\r\x12\x12\n\ntruncation\x18\x06 \x01(\x01\"\xf6\x01\n\x17\x42oundingBox3DAnnotation\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\r\x12%\n\x03\x62ox\x18\x02 \x01(\x0b\x32\x18.dgp.proto.BoundingBox3D\x12\x13\n\x0binstance_id\x18\x03 \x01(\r\x12\x46\n\nattributes\x18\x04 \x03(\x0b\x32\x32.dgp.proto.BoundingBox3DAnnotation.AttributesEntry\x12\x12\n\nnum_points\x18\x05 \x01(\r\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"S\n\x18\x42oundingBox2DAnnotations\x12\x37\n\x0b\x61nnotations\x18\x01 \x03(\x0b\x32\".dgp.proto.BoundingBox2DAnnotation\"S\n\x18\x42oundingBox3DAnnotations\x12\x37\n\x0b\x61nnotations\x18\x01 \x03(\x0b\x32\".dgp.proto.BoundingBox3DAnnotation*\x9b\x02\n\x0e\x41nnotationType\x12\x13\n\x0f\x42OUNDING_BOX_2D\x10\x00\x12\x13\n\x0f\x42OUNDING_BOX_3D\x10\x01\x12\x1c\n\x18SEMANTIC_SEGMENTATION_2D\x10\x02\x12\x1c\n\x18SEMANTIC_SEGMENTATION_3D\x10\x03\x12\x1c\n\x18INSTANCE_SEGMENTATION_2D\x10\x04\x12\x1c\n\x18INSTANCE_SEGMENTATION_3D\x10\x05\x12\t\n\x05\x44\x45PTH\x10\x06\x12\x16\n\x12SURFACE_NORMALS_2D\x10\n\x12\x16\n\x12SURFACE_NORMALS_3D\x10\x07\x12\x15\n\x11MOTION_VECTORS_2D\x10\x08\x12\x15\n\x11MOTION_VECTORS_3D\x10\tb\x06proto3')
  ,
  dependencies=[dgp_dot_proto_dot_geometry__pb2.DESCRIPTOR,])

_ANNOTATIONTYPE = _descriptor.EnumDescriptor(
  name='AnnotationType',
  full_name='dgp.proto.AnnotationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOUNDING_BOX_2D', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOUNDING_BOX_3D', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEMANTIC_SEGMENTATION_2D', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEMANTIC_SEGMENTATION_3D', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTANCE_SEGMENTATION_2D', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTANCE_SEGMENTATION_3D', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPTH', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SURFACE_NORMALS_2D', index=7, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SURFACE_NORMALS_3D', index=8, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOTION_VECTORS_2D', index=9, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOTION_VECTORS_3D', index=10, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=944,
  serialized_end=1227,
)
_sym_db.RegisterEnumDescriptor(_ANNOTATIONTYPE)

AnnotationType = enum_type_wrapper.EnumTypeWrapper(_ANNOTATIONTYPE)
BOUNDING_BOX_2D = 0
BOUNDING_BOX_3D = 1
SEMANTIC_SEGMENTATION_2D = 2
SEMANTIC_SEGMENTATION_3D = 3
INSTANCE_SEGMENTATION_2D = 4
INSTANCE_SEGMENTATION_3D = 5
DEPTH = 6
SURFACE_NORMALS_2D = 10
SURFACE_NORMALS_3D = 7
MOTION_VECTORS_2D = 8
MOTION_VECTORS_3D = 9



_BOUNDINGBOX2D = _descriptor.Descriptor(
  name='BoundingBox2D',
  full_name='dgp.proto.BoundingBox2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='dgp.proto.BoundingBox2D.x', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='dgp.proto.BoundingBox2D.y', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='dgp.proto.BoundingBox2D.w', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='h', full_name='dgp.proto.BoundingBox2D.h', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=68,
  serialized_end=127,
)


_BOUNDINGBOX2DANNOTATION_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='dgp.proto.BoundingBox2DAnnotation.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dgp.proto.BoundingBox2DAnnotation.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dgp.proto.BoundingBox2DAnnotation.AttributesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=387,
)

_BOUNDINGBOX2DANNOTATION = _descriptor.Descriptor(
  name='BoundingBox2DAnnotation',
  full_name='dgp.proto.BoundingBox2DAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_id', full_name='dgp.proto.BoundingBox2DAnnotation.class_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='box', full_name='dgp.proto.BoundingBox2DAnnotation.box', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='area', full_name='dgp.proto.BoundingBox2DAnnotation.area', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iscrowd', full_name='dgp.proto.BoundingBox2DAnnotation.iscrowd', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='dgp.proto.BoundingBox2DAnnotation.instance_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='dgp.proto.BoundingBox2DAnnotation.attributes', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BOUNDINGBOX2DANNOTATION_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=387,
)


_BOUNDINGBOX3D = _descriptor.Descriptor(
  name='BoundingBox3D',
  full_name='dgp.proto.BoundingBox3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pose', full_name='dgp.proto.BoundingBox3D.pose', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='dgp.proto.BoundingBox3D.width', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='dgp.proto.BoundingBox3D.length', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='dgp.proto.BoundingBox3D.height', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occlusion', full_name='dgp.proto.BoundingBox3D.occlusion', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truncation', full_name='dgp.proto.BoundingBox3D.truncation', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=390,
  serialized_end=522,
)


_BOUNDINGBOX3DANNOTATION_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='dgp.proto.BoundingBox3DAnnotation.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dgp.proto.BoundingBox3DAnnotation.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dgp.proto.BoundingBox3DAnnotation.AttributesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=387,
)

_BOUNDINGBOX3DANNOTATION = _descriptor.Descriptor(
  name='BoundingBox3DAnnotation',
  full_name='dgp.proto.BoundingBox3DAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_id', full_name='dgp.proto.BoundingBox3DAnnotation.class_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='box', full_name='dgp.proto.BoundingBox3DAnnotation.box', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='dgp.proto.BoundingBox3DAnnotation.instance_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='dgp.proto.BoundingBox3DAnnotation.attributes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_points', full_name='dgp.proto.BoundingBox3DAnnotation.num_points', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BOUNDINGBOX3DANNOTATION_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=525,
  serialized_end=771,
)


_BOUNDINGBOX2DANNOTATIONS = _descriptor.Descriptor(
  name='BoundingBox2DAnnotations',
  full_name='dgp.proto.BoundingBox2DAnnotations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotations', full_name='dgp.proto.BoundingBox2DAnnotations.annotations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=773,
  serialized_end=856,
)


_BOUNDINGBOX3DANNOTATIONS = _descriptor.Descriptor(
  name='BoundingBox3DAnnotations',
  full_name='dgp.proto.BoundingBox3DAnnotations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotations', full_name='dgp.proto.BoundingBox3DAnnotations.annotations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=858,
  serialized_end=941,
)

_BOUNDINGBOX2DANNOTATION_ATTRIBUTESENTRY.containing_type = _BOUNDINGBOX2DANNOTATION
_BOUNDINGBOX2DANNOTATION.fields_by_name['box'].message_type = _BOUNDINGBOX2D
_BOUNDINGBOX2DANNOTATION.fields_by_name['attributes'].message_type = _BOUNDINGBOX2DANNOTATION_ATTRIBUTESENTRY
_BOUNDINGBOX3D.fields_by_name['pose'].message_type = dgp_dot_proto_dot_geometry__pb2._POSE
_BOUNDINGBOX3DANNOTATION_ATTRIBUTESENTRY.containing_type = _BOUNDINGBOX3DANNOTATION
_BOUNDINGBOX3DANNOTATION.fields_by_name['box'].message_type = _BOUNDINGBOX3D
_BOUNDINGBOX3DANNOTATION.fields_by_name['attributes'].message_type = _BOUNDINGBOX3DANNOTATION_ATTRIBUTESENTRY
_BOUNDINGBOX2DANNOTATIONS.fields_by_name['annotations'].message_type = _BOUNDINGBOX2DANNOTATION
_BOUNDINGBOX3DANNOTATIONS.fields_by_name['annotations'].message_type = _BOUNDINGBOX3DANNOTATION
DESCRIPTOR.message_types_by_name['BoundingBox2D'] = _BOUNDINGBOX2D
DESCRIPTOR.message_types_by_name['BoundingBox2DAnnotation'] = _BOUNDINGBOX2DANNOTATION
DESCRIPTOR.message_types_by_name['BoundingBox3D'] = _BOUNDINGBOX3D
DESCRIPTOR.message_types_by_name['BoundingBox3DAnnotation'] = _BOUNDINGBOX3DANNOTATION
DESCRIPTOR.message_types_by_name['BoundingBox2DAnnotations'] = _BOUNDINGBOX2DANNOTATIONS
DESCRIPTOR.message_types_by_name['BoundingBox3DAnnotations'] = _BOUNDINGBOX3DANNOTATIONS
DESCRIPTOR.enum_types_by_name['AnnotationType'] = _ANNOTATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BoundingBox2D = _reflection.GeneratedProtocolMessageType('BoundingBox2D', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDINGBOX2D,
  __module__ = 'dgp.proto.annotations_pb2'
  # @@protoc_insertion_point(class_scope:dgp.proto.BoundingBox2D)
  ))
_sym_db.RegisterMessage(BoundingBox2D)

BoundingBox2DAnnotation = _reflection.GeneratedProtocolMessageType('BoundingBox2DAnnotation', (_message.Message,), dict(

  AttributesEntry = _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), dict(
    DESCRIPTOR = _BOUNDINGBOX2DANNOTATION_ATTRIBUTESENTRY,
    __module__ = 'dgp.proto.annotations_pb2'
    # @@protoc_insertion_point(class_scope:dgp.proto.BoundingBox2DAnnotation.AttributesEntry)
    ))
  ,
  DESCRIPTOR = _BOUNDINGBOX2DANNOTATION,
  __module__ = 'dgp.proto.annotations_pb2'
  # @@protoc_insertion_point(class_scope:dgp.proto.BoundingBox2DAnnotation)
  ))
_sym_db.RegisterMessage(BoundingBox2DAnnotation)
_sym_db.RegisterMessage(BoundingBox2DAnnotation.AttributesEntry)

BoundingBox3D = _reflection.GeneratedProtocolMessageType('BoundingBox3D', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDINGBOX3D,
  __module__ = 'dgp.proto.annotations_pb2'
  # @@protoc_insertion_point(class_scope:dgp.proto.BoundingBox3D)
  ))
_sym_db.RegisterMessage(BoundingBox3D)

BoundingBox3DAnnotation = _reflection.GeneratedProtocolMessageType('BoundingBox3DAnnotation', (_message.Message,), dict(

  AttributesEntry = _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), dict(
    DESCRIPTOR = _BOUNDINGBOX3DANNOTATION_ATTRIBUTESENTRY,
    __module__ = 'dgp.proto.annotations_pb2'
    # @@protoc_insertion_point(class_scope:dgp.proto.BoundingBox3DAnnotation.AttributesEntry)
    ))
  ,
  DESCRIPTOR = _BOUNDINGBOX3DANNOTATION,
  __module__ = 'dgp.proto.annotations_pb2'
  # @@protoc_insertion_point(class_scope:dgp.proto.BoundingBox3DAnnotation)
  ))
_sym_db.RegisterMessage(BoundingBox3DAnnotation)
_sym_db.RegisterMessage(BoundingBox3DAnnotation.AttributesEntry)

BoundingBox2DAnnotations = _reflection.GeneratedProtocolMessageType('BoundingBox2DAnnotations', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDINGBOX2DANNOTATIONS,
  __module__ = 'dgp.proto.annotations_pb2'
  # @@protoc_insertion_point(class_scope:dgp.proto.BoundingBox2DAnnotations)
  ))
_sym_db.RegisterMessage(BoundingBox2DAnnotations)

BoundingBox3DAnnotations = _reflection.GeneratedProtocolMessageType('BoundingBox3DAnnotations', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDINGBOX3DANNOTATIONS,
  __module__ = 'dgp.proto.annotations_pb2'
  # @@protoc_insertion_point(class_scope:dgp.proto.BoundingBox3DAnnotations)
  ))
_sym_db.RegisterMessage(BoundingBox3DAnnotations)


_BOUNDINGBOX2DANNOTATION_ATTRIBUTESENTRY._options = None
_BOUNDINGBOX3DANNOTATION_ATTRIBUTESENTRY._options = None
# @@protoc_insertion_point(module_scope)