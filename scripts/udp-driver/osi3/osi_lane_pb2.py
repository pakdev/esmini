# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osi3/osi_lane.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from osi3 import osi_common_pb2 as osi3_dot_osi__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='osi3/osi_lane.proto',
  package='osi3',
  syntax='proto3',
  serialized_options=b'H\001',
  serialized_pb=b'\n\x13osi3/osi_lane.proto\x12\x04osi3\x1a\x15osi3/osi_common.proto\"\xf7\n\n\x04Lane\x12\x1c\n\x02id\x18\x01 \x01(\x0b\x32\x10.osi3.Identifier\x12\x31\n\x0e\x63lassification\x18\x02 \x01(\x0b\x32\x19.osi3.Lane.Classification\x1a\x9d\n\n\x0e\x43lassification\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.osi3.Lane.Classification.Type\x12\x1c\n\x14is_host_vehicle_lane\x18\x02 \x01(\x08\x12\"\n\ncenterline\x18\x03 \x03(\x0b\x32\x0e.osi3.Vector3d\x12\'\n\x1f\x63\x65nterline_is_driving_direction\x18\x04 \x01(\x08\x12/\n\x15left_adjacent_lane_id\x18\x05 \x03(\x0b\x32\x10.osi3.Identifier\x12\x30\n\x16right_adjacent_lane_id\x18\x06 \x03(\x0b\x32\x10.osi3.Identifier\x12;\n\x0clane_pairing\x18\x07 \x03(\x0b\x32%.osi3.Lane.Classification.LanePairing\x12\x30\n\x16right_lane_boundary_id\x18\x08 \x03(\x0b\x32\x10.osi3.Identifier\x12/\n\x15left_lane_boundary_id\x18\t \x03(\x0b\x32\x10.osi3.Identifier\x12/\n\x15\x66ree_lane_boundary_id\x18\n \x03(\x0b\x32\x10.osi3.Identifier\x12?\n\x0eroad_condition\x18\x0b \x01(\x0b\x32\'.osi3.Lane.Classification.RoadCondition\x12\x32\n\x07subtype\x18\x0c \x01(\x0e\x32!.osi3.Lane.Classification.Subtype\x1a\xb1\x01\n\rRoadCondition\x12\x1b\n\x13surface_temperature\x18\x01 \x01(\x01\x12\x1a\n\x12surface_water_film\x18\x02 \x01(\x01\x12\x1e\n\x16surface_freezing_point\x18\x03 \x01(\x01\x12\x13\n\x0bsurface_ice\x18\x04 \x01(\x01\x12\x19\n\x11surface_roughness\x18\x05 \x01(\x01\x12\x17\n\x0fsurface_texture\x18\x06 \x01(\x01\x1ah\n\x0bLanePairing\x12,\n\x12\x61ntecessor_lane_id\x18\x01 \x01(\x0b\x32\x10.osi3.Identifier\x12+\n\x11successor_lane_id\x18\x02 \x01(\x0b\x32\x10.osi3.Identifier\"f\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x0e\n\nTYPE_OTHER\x10\x01\x12\x10\n\x0cTYPE_DRIVING\x10\x02\x12\x13\n\x0fTYPE_NONDRIVING\x10\x03\x12\x15\n\x11TYPE_INTERSECTION\x10\x04\"\xc2\x02\n\x07Subtype\x12\x13\n\x0fSUBTYPE_UNKNOWN\x10\x00\x12\x11\n\rSUBTYPE_OTHER\x10\x01\x12\x12\n\x0eSUBTYPE_NORMAL\x10\x02\x12\x12\n\x0eSUBTYPE_BIKING\x10\x03\x12\x14\n\x10SUBTYPE_SIDEWALK\x10\x04\x12\x13\n\x0fSUBTYPE_PARKING\x10\x05\x12\x10\n\x0cSUBTYPE_STOP\x10\x06\x12\x16\n\x12SUBTYPE_RESTRICTED\x10\x07\x12\x12\n\x0eSUBTYPE_BORDER\x10\x08\x12\x14\n\x10SUBTYPE_SHOULDER\x10\t\x12\x10\n\x0cSUBTYPE_EXIT\x10\n\x12\x11\n\rSUBTYPE_ENTRY\x10\x0b\x12\x12\n\x0eSUBTYPE_ONRAMP\x10\x0c\x12\x13\n\x0fSUBTYPE_OFFRAMP\x10\r\x12\x1a\n\x16SUBTYPE_CONNECTINGRAMP\x10\x0e\"\xe3\x06\n\x0cLaneBoundary\x12\x1c\n\x02id\x18\x01 \x01(\x0b\x32\x10.osi3.Identifier\x12\x37\n\rboundary_line\x18\x02 \x03(\x0b\x32 .osi3.LaneBoundary.BoundaryPoint\x12\x39\n\x0e\x63lassification\x18\x03 \x01(\x0b\x32!.osi3.LaneBoundary.Classification\x1aP\n\rBoundaryPoint\x12 \n\x08position\x18\x01 \x01(\x0b\x32\x0e.osi3.Vector3d\x12\r\n\x05width\x18\x02 \x01(\x01\x12\x0e\n\x06height\x18\x03 \x01(\x01\x1a\xee\x04\n\x0e\x43lassification\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.osi3.LaneBoundary.Classification.Type\x12\x36\n\x05\x63olor\x18\x02 \x01(\x0e\x32\'.osi3.LaneBoundary.Classification.Color\x12/\n\x15limiting_structure_id\x18\x03 \x03(\x0b\x32\x10.osi3.Identifier\"\x99\x02\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x0e\n\nTYPE_OTHER\x10\x01\x12\x10\n\x0cTYPE_NO_LINE\x10\x02\x12\x13\n\x0fTYPE_SOLID_LINE\x10\x03\x12\x14\n\x10TYPE_DASHED_LINE\x10\x04\x12\x13\n\x0fTYPE_BOTTS_DOTS\x10\x05\x12\x12\n\x0eTYPE_ROAD_EDGE\x10\x06\x12\x12\n\x0eTYPE_SNOW_EDGE\x10\x07\x12\x13\n\x0fTYPE_GRASS_EDGE\x10\x08\x12\x14\n\x10TYPE_GRAVEL_EDGE\x10\t\x12\x12\n\x0eTYPE_SOIL_EDGE\x10\n\x12\x13\n\x0fTYPE_GUARD_RAIL\x10\x0b\x12\r\n\tTYPE_CURB\x10\x0c\x12\x12\n\x0eTYPE_STRUCTURE\x10\r\"\xa0\x01\n\x05\x43olor\x12\x11\n\rCOLOR_UNKNOWN\x10\x00\x12\x0f\n\x0b\x43OLOR_OTHER\x10\x01\x12\x0e\n\nCOLOR_NONE\x10\x02\x12\x0f\n\x0b\x43OLOR_WHITE\x10\x03\x12\x10\n\x0c\x43OLOR_YELLOW\x10\x04\x12\r\n\tCOLOR_RED\x10\x05\x12\x0e\n\nCOLOR_BLUE\x10\x06\x12\x0f\n\x0b\x43OLOR_GREEN\x10\x07\x12\x10\n\x0c\x43OLOR_VIOLET\x10\x08\x42\x02H\x01\x62\x06proto3'
  ,
  dependencies=[osi3_dot_osi__common__pb2.DESCRIPTOR,])



_LANE_CLASSIFICATION_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='osi3.Lane.Classification.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_OTHER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_DRIVING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_NONDRIVING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_INTERSECTION', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1025,
  serialized_end=1127,
)
_sym_db.RegisterEnumDescriptor(_LANE_CLASSIFICATION_TYPE)

_LANE_CLASSIFICATION_SUBTYPE = _descriptor.EnumDescriptor(
  name='Subtype',
  full_name='osi3.Lane.Classification.Subtype',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_OTHER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_NORMAL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_BIKING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_SIDEWALK', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_PARKING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_STOP', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_RESTRICTED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_BORDER', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_SHOULDER', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_EXIT', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_ENTRY', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_ONRAMP', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_OFFRAMP', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_CONNECTINGRAMP', index=14, number=14,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1130,
  serialized_end=1452,
)
_sym_db.RegisterEnumDescriptor(_LANE_CLASSIFICATION_SUBTYPE)

_LANEBOUNDARY_CLASSIFICATION_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='osi3.LaneBoundary.Classification.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_OTHER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_NO_LINE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SOLID_LINE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_DASHED_LINE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_BOTTS_DOTS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_ROAD_EDGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SNOW_EDGE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_GRASS_EDGE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_GRAVEL_EDGE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SOIL_EDGE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_GUARD_RAIL', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_CURB', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_STRUCTURE', index=13, number=13,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1878,
  serialized_end=2159,
)
_sym_db.RegisterEnumDescriptor(_LANEBOUNDARY_CLASSIFICATION_TYPE)

_LANEBOUNDARY_CLASSIFICATION_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='osi3.LaneBoundary.Classification.Color',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COLOR_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_OTHER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_NONE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_WHITE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_YELLOW', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_RED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_BLUE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_GREEN', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_VIOLET', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2162,
  serialized_end=2322,
)
_sym_db.RegisterEnumDescriptor(_LANEBOUNDARY_CLASSIFICATION_COLOR)


_LANE_CLASSIFICATION_ROADCONDITION = _descriptor.Descriptor(
  name='RoadCondition',
  full_name='osi3.Lane.Classification.RoadCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='surface_temperature', full_name='osi3.Lane.Classification.RoadCondition.surface_temperature', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='surface_water_film', full_name='osi3.Lane.Classification.RoadCondition.surface_water_film', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='surface_freezing_point', full_name='osi3.Lane.Classification.RoadCondition.surface_freezing_point', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='surface_ice', full_name='osi3.Lane.Classification.RoadCondition.surface_ice', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='surface_roughness', full_name='osi3.Lane.Classification.RoadCondition.surface_roughness', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='surface_texture', full_name='osi3.Lane.Classification.RoadCondition.surface_texture', index=5,
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
  serialized_start=740,
  serialized_end=917,
)

_LANE_CLASSIFICATION_LANEPAIRING = _descriptor.Descriptor(
  name='LanePairing',
  full_name='osi3.Lane.Classification.LanePairing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='antecessor_lane_id', full_name='osi3.Lane.Classification.LanePairing.antecessor_lane_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='successor_lane_id', full_name='osi3.Lane.Classification.LanePairing.successor_lane_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=919,
  serialized_end=1023,
)

_LANE_CLASSIFICATION = _descriptor.Descriptor(
  name='Classification',
  full_name='osi3.Lane.Classification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='osi3.Lane.Classification.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_host_vehicle_lane', full_name='osi3.Lane.Classification.is_host_vehicle_lane', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='centerline', full_name='osi3.Lane.Classification.centerline', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='centerline_is_driving_direction', full_name='osi3.Lane.Classification.centerline_is_driving_direction', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_adjacent_lane_id', full_name='osi3.Lane.Classification.left_adjacent_lane_id', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_adjacent_lane_id', full_name='osi3.Lane.Classification.right_adjacent_lane_id', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_pairing', full_name='osi3.Lane.Classification.lane_pairing', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_lane_boundary_id', full_name='osi3.Lane.Classification.right_lane_boundary_id', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_lane_boundary_id', full_name='osi3.Lane.Classification.left_lane_boundary_id', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_lane_boundary_id', full_name='osi3.Lane.Classification.free_lane_boundary_id', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='road_condition', full_name='osi3.Lane.Classification.road_condition', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='osi3.Lane.Classification.subtype', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LANE_CLASSIFICATION_ROADCONDITION, _LANE_CLASSIFICATION_LANEPAIRING, ],
  enum_types=[
    _LANE_CLASSIFICATION_TYPE,
    _LANE_CLASSIFICATION_SUBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=1452,
)

_LANE = _descriptor.Descriptor(
  name='Lane',
  full_name='osi3.Lane',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='osi3.Lane.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classification', full_name='osi3.Lane.classification', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LANE_CLASSIFICATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=1452,
)


_LANEBOUNDARY_BOUNDARYPOINT = _descriptor.Descriptor(
  name='BoundaryPoint',
  full_name='osi3.LaneBoundary.BoundaryPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='osi3.LaneBoundary.BoundaryPoint.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='osi3.LaneBoundary.BoundaryPoint.width', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='osi3.LaneBoundary.BoundaryPoint.height', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=1617,
  serialized_end=1697,
)

_LANEBOUNDARY_CLASSIFICATION = _descriptor.Descriptor(
  name='Classification',
  full_name='osi3.LaneBoundary.Classification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='osi3.LaneBoundary.Classification.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='osi3.LaneBoundary.Classification.color', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limiting_structure_id', full_name='osi3.LaneBoundary.Classification.limiting_structure_id', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LANEBOUNDARY_CLASSIFICATION_TYPE,
    _LANEBOUNDARY_CLASSIFICATION_COLOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1700,
  serialized_end=2322,
)

_LANEBOUNDARY = _descriptor.Descriptor(
  name='LaneBoundary',
  full_name='osi3.LaneBoundary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='osi3.LaneBoundary.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boundary_line', full_name='osi3.LaneBoundary.boundary_line', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classification', full_name='osi3.LaneBoundary.classification', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LANEBOUNDARY_BOUNDARYPOINT, _LANEBOUNDARY_CLASSIFICATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1455,
  serialized_end=2322,
)

_LANE_CLASSIFICATION_ROADCONDITION.containing_type = _LANE_CLASSIFICATION
_LANE_CLASSIFICATION_LANEPAIRING.fields_by_name['antecessor_lane_id'].message_type = osi3_dot_osi__common__pb2._IDENTIFIER
_LANE_CLASSIFICATION_LANEPAIRING.fields_by_name['successor_lane_id'].message_type = osi3_dot_osi__common__pb2._IDENTIFIER
_LANE_CLASSIFICATION_LANEPAIRING.containing_type = _LANE_CLASSIFICATION
_LANE_CLASSIFICATION.fields_by_name['type'].enum_type = _LANE_CLASSIFICATION_TYPE
_LANE_CLASSIFICATION.fields_by_name['centerline'].message_type = osi3_dot_osi__common__pb2._VECTOR3D
_LANE_CLASSIFICATION.fields_by_name['left_adjacent_lane_id'].message_type = osi3_dot_osi__common__pb2._IDENTIFIER
_LANE_CLASSIFICATION.fields_by_name['right_adjacent_lane_id'].message_type = osi3_dot_osi__common__pb2._IDENTIFIER
_LANE_CLASSIFICATION.fields_by_name['lane_pairing'].message_type = _LANE_CLASSIFICATION_LANEPAIRING
_LANE_CLASSIFICATION.fields_by_name['right_lane_boundary_id'].message_type = osi3_dot_osi__common__pb2._IDENTIFIER
_LANE_CLASSIFICATION.fields_by_name['left_lane_boundary_id'].message_type = osi3_dot_osi__common__pb2._IDENTIFIER
_LANE_CLASSIFICATION.fields_by_name['free_lane_boundary_id'].message_type = osi3_dot_osi__common__pb2._IDENTIFIER
_LANE_CLASSIFICATION.fields_by_name['road_condition'].message_type = _LANE_CLASSIFICATION_ROADCONDITION
_LANE_CLASSIFICATION.fields_by_name['subtype'].enum_type = _LANE_CLASSIFICATION_SUBTYPE
_LANE_CLASSIFICATION.containing_type = _LANE
_LANE_CLASSIFICATION_TYPE.containing_type = _LANE_CLASSIFICATION
_LANE_CLASSIFICATION_SUBTYPE.containing_type = _LANE_CLASSIFICATION
_LANE.fields_by_name['id'].message_type = osi3_dot_osi__common__pb2._IDENTIFIER
_LANE.fields_by_name['classification'].message_type = _LANE_CLASSIFICATION
_LANEBOUNDARY_BOUNDARYPOINT.fields_by_name['position'].message_type = osi3_dot_osi__common__pb2._VECTOR3D
_LANEBOUNDARY_BOUNDARYPOINT.containing_type = _LANEBOUNDARY
_LANEBOUNDARY_CLASSIFICATION.fields_by_name['type'].enum_type = _LANEBOUNDARY_CLASSIFICATION_TYPE
_LANEBOUNDARY_CLASSIFICATION.fields_by_name['color'].enum_type = _LANEBOUNDARY_CLASSIFICATION_COLOR
_LANEBOUNDARY_CLASSIFICATION.fields_by_name['limiting_structure_id'].message_type = osi3_dot_osi__common__pb2._IDENTIFIER
_LANEBOUNDARY_CLASSIFICATION.containing_type = _LANEBOUNDARY
_LANEBOUNDARY_CLASSIFICATION_TYPE.containing_type = _LANEBOUNDARY_CLASSIFICATION
_LANEBOUNDARY_CLASSIFICATION_COLOR.containing_type = _LANEBOUNDARY_CLASSIFICATION
_LANEBOUNDARY.fields_by_name['id'].message_type = osi3_dot_osi__common__pb2._IDENTIFIER
_LANEBOUNDARY.fields_by_name['boundary_line'].message_type = _LANEBOUNDARY_BOUNDARYPOINT
_LANEBOUNDARY.fields_by_name['classification'].message_type = _LANEBOUNDARY_CLASSIFICATION
DESCRIPTOR.message_types_by_name['Lane'] = _LANE
DESCRIPTOR.message_types_by_name['LaneBoundary'] = _LANEBOUNDARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Lane = _reflection.GeneratedProtocolMessageType('Lane', (_message.Message,), {

  'Classification' : _reflection.GeneratedProtocolMessageType('Classification', (_message.Message,), {

    'RoadCondition' : _reflection.GeneratedProtocolMessageType('RoadCondition', (_message.Message,), {
      'DESCRIPTOR' : _LANE_CLASSIFICATION_ROADCONDITION,
      '__module__' : 'osi3.osi_lane_pb2'
      # @@protoc_insertion_point(class_scope:osi3.Lane.Classification.RoadCondition)
      })
    ,

    'LanePairing' : _reflection.GeneratedProtocolMessageType('LanePairing', (_message.Message,), {
      'DESCRIPTOR' : _LANE_CLASSIFICATION_LANEPAIRING,
      '__module__' : 'osi3.osi_lane_pb2'
      # @@protoc_insertion_point(class_scope:osi3.Lane.Classification.LanePairing)
      })
    ,
    'DESCRIPTOR' : _LANE_CLASSIFICATION,
    '__module__' : 'osi3.osi_lane_pb2'
    # @@protoc_insertion_point(class_scope:osi3.Lane.Classification)
    })
  ,
  'DESCRIPTOR' : _LANE,
  '__module__' : 'osi3.osi_lane_pb2'
  # @@protoc_insertion_point(class_scope:osi3.Lane)
  })
_sym_db.RegisterMessage(Lane)
_sym_db.RegisterMessage(Lane.Classification)
_sym_db.RegisterMessage(Lane.Classification.RoadCondition)
_sym_db.RegisterMessage(Lane.Classification.LanePairing)

LaneBoundary = _reflection.GeneratedProtocolMessageType('LaneBoundary', (_message.Message,), {

  'BoundaryPoint' : _reflection.GeneratedProtocolMessageType('BoundaryPoint', (_message.Message,), {
    'DESCRIPTOR' : _LANEBOUNDARY_BOUNDARYPOINT,
    '__module__' : 'osi3.osi_lane_pb2'
    # @@protoc_insertion_point(class_scope:osi3.LaneBoundary.BoundaryPoint)
    })
  ,

  'Classification' : _reflection.GeneratedProtocolMessageType('Classification', (_message.Message,), {
    'DESCRIPTOR' : _LANEBOUNDARY_CLASSIFICATION,
    '__module__' : 'osi3.osi_lane_pb2'
    # @@protoc_insertion_point(class_scope:osi3.LaneBoundary.Classification)
    })
  ,
  'DESCRIPTOR' : _LANEBOUNDARY,
  '__module__' : 'osi3.osi_lane_pb2'
  # @@protoc_insertion_point(class_scope:osi3.LaneBoundary)
  })
_sym_db.RegisterMessage(LaneBoundary)
_sym_db.RegisterMessage(LaneBoundary.BoundaryPoint)
_sym_db.RegisterMessage(LaneBoundary.Classification)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
