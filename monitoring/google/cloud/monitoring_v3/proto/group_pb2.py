# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_v3/proto/group.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_v3/proto/group.proto",
    package="google.monitoring.v3",
    syntax="proto3",
    serialized_options=_b(
        "\n\030com.google.monitoring.v3B\nGroupProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3"
    ),
    serialized_pb=_b(
        '\n,google/cloud/monitoring_v3/proto/group.proto\x12\x14google.monitoring.v3\x1a\x19google/api/resource.proto"\x80\x02\n\x05Group\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0bparent_name\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12\x12\n\nis_cluster\x18\x06 \x01(\x08:\x99\x01\xea\x41\x95\x01\n\x1fmonitoring.googleapis.com/Group\x12!projects/{project}/groups/{group}\x12+organizations/{organization}/groups/{group}\x12\x1f\x66olders/{folder}/groups/{group}\x12\x01*B\xa2\x01\n\x18\x63om.google.monitoring.v3B\nGroupProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3b\x06proto3'
    ),
    dependencies=[google_dot_api_dot_resource__pb2.DESCRIPTOR],
)


_GROUP = _descriptor.Descriptor(
    name="Group",
    full_name="google.monitoring.v3.Group",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.v3.Group.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.monitoring.v3.Group.display_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="parent_name",
            full_name="google.monitoring.v3.Group.parent_name",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="filter",
            full_name="google.monitoring.v3.Group.filter",
            index=3,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="is_cluster",
            full_name="google.monitoring.v3.Group.is_cluster",
            index=4,
            number=6,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b(
        "\352A\225\001\n\037monitoring.googleapis.com/Group\022!projects/{project}/groups/{group}\022+organizations/{organization}/groups/{group}\022\037folders/{folder}/groups/{group}\022\001*"
    ),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=98,
    serialized_end=354,
)

DESCRIPTOR.message_types_by_name["Group"] = _GROUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Group = _reflection.GeneratedProtocolMessageType(
    "Group",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GROUP,
        __module__="google.cloud.monitoring_v3.proto.group_pb2",
        __doc__="""The description of a dynamic collection of monitored
  resources. Each group has a filter that is matched against monitored
  resources and their associated metadata. If a group's filter matches an
  available monitored resource, then that resource is a member of that
  group. Groups can contain any number of monitored resources, and each
  monitored resource can be a member of any number of groups.
  
  Groups can be nested in parent-child hierarchies. The ``parentName``
  field identifies an optional parent for each group. If a group has a
  parent, then the only monitored resources available to be matched by the
  group's filter are the resources contained in the parent group. In other
  words, a group contains the monitored resources that match its filter
  and the filters of all the group's ancestors. A group without a parent
  can contain any monitored resource.
  
  For example, consider an infrastructure running a set of instances with
  two user-defined tags: ``"environment"`` and ``"role"``. A parent group
  has a filter, ``environment="production"``. A child of that parent group
  has a filter, ``role="transcoder"``. The parent group contains all
  instances in the production environment, regardless of their roles. The
  child group contains instances that have the transcoder role *and* are
  in the production environment.
  
  The monitored resources contained in a group can change at any moment,
  depending on what resources exist and what filters are associated with
  the group and its ancestors.
  
  
  Attributes:
      name:
          Output only. The name of this group. The format is
          ``"projects/{project_id_or_number}/groups/{group_id}"``. When
          creating a group, this field is ignored and a new name is
          created consisting of the project specified in the call to
          ``CreateGroup`` and a unique ``{group_id}`` that is generated
          automatically.
      display_name:
          A user-assigned name for this group, used only for display
          purposes.
      parent_name:
          The name of the group's parent, if it has one. The format is
          ``"projects/{project_id_or_number}/groups/{group_id}"``. For
          groups with no parent, ``parentName`` is the empty string,
          ``""``.
      filter:
          The filter used to determine which monitored resources belong
          to this group.
      is_cluster:
          If true, the members of this group are considered to be a
          cluster. The system can perform additional analysis on groups
          that are clusters.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.Group)
    ),
)
_sym_db.RegisterMessage(Group)


DESCRIPTOR._options = None
_GROUP._options = None
# @@protoc_insertion_point(module_scope)
