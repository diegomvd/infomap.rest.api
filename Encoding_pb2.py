# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Encoding.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x45ncoding.proto\x12*org.integratedmodelling.klab.data.encoding\"\x94\x0c\n\x08KlabData\x12\x10\n\x08geometry\x18\x01 \x01(\t\x12\x11\n\tsemantics\x18\x02 \x01(\t\x12\x0f\n\x07\x65lapsed\x18\x03 \x01(\x03\x12X\n\rnotifications\x18\x04 \x03(\x0b\x32\x41.org.integratedmodelling.klab.data.encoding.KlabData.Notification\x12L\n\x07objects\x18\x05 \x03(\x0b\x32;.org.integratedmodelling.klab.data.encoding.KlabData.Object\x12J\n\x06states\x18\x06 \x03(\x0b\x32:.org.integratedmodelling.klab.data.encoding.KlabData.State\x12\x10\n\x08noChange\x18\x07 \x01(\x05\x1am\n\x0cNotification\x12\x0c\n\x04text\x18\x01 \x01(\t\x12O\n\x08severity\x18\x02 \x01(\x0e\x32=.org.integratedmodelling.klab.data.encoding.KlabData.Severity\x1a\xe4\x03\n\x06Object\x12\x0c\n\x04name\x18\x01 \x01(\t\x12_\n\nproperties\x18\x02 \x03(\x0b\x32K.org.integratedmodelling.klab.data.encoding.KlabData.Object.PropertiesEntry\x12J\n\x06states\x18\x03 \x03(\x0b\x32:.org.integratedmodelling.klab.data.encoding.KlabData.State\x12L\n\x07objects\x18\x04 \x03(\x0b\x32;.org.integratedmodelling.klab.data.encoding.KlabData.Object\x12\x10\n\x08geometry\x18\x05 \x01(\t\x12[\n\x08metadata\x18\x06 \x03(\x0b\x32I.org.integratedmodelling.klab.data.encoding.KlabData.Object.MetadataEntry\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x97\x01\n\x0bLookupTable\x12Z\n\x05table\x18\x01 \x03(\x0b\x32K.org.integratedmodelling.klab.data.encoding.KlabData.LookupTable.TableEntry\x1a,\n\nTableEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xa2\x03\n\x05State\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tsemantics\x18\x02 \x01(\t\x12\x12\n\ndoubledata\x18\x03 \x03(\x01\x12\x11\n\ttabledata\x18\x04 \x03(\r\x12\x0f\n\x07intdata\x18\x05 \x03(\x12\x12\x13\n\x0b\x62ooleandata\x18\x06 \x03(\x08\x12O\n\x05table\x18\x07 \x01(\x0b\x32@.org.integratedmodelling.klab.data.encoding.KlabData.LookupTable\x12\x1d\n\x15\x65xternalDatasourceUrl\x18\x08 \x01(\t\x12Z\n\x08metadata\x18\t \x03(\x0b\x32H.org.integratedmodelling.klab.data.encoding.KlabData.State.MetadataEntry\x12\x12\n\nstringdata\x18\n \x03(\t\x12\x1a\n\x12stringdataencoding\x18\x0b \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"7\n\x08Severity\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\t\n\x05\x44\x45\x42UG\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Encoding_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _KLABDATA_OBJECT_PROPERTIESENTRY._options = None
  _KLABDATA_OBJECT_PROPERTIESENTRY._serialized_options = b'8\001'
  _KLABDATA_OBJECT_METADATAENTRY._options = None
  _KLABDATA_OBJECT_METADATAENTRY._serialized_options = b'8\001'
  _KLABDATA_LOOKUPTABLE_TABLEENTRY._options = None
  _KLABDATA_LOOKUPTABLE_TABLEENTRY._serialized_options = b'8\001'
  _KLABDATA_STATE_METADATAENTRY._options = None
  _KLABDATA_STATE_METADATAENTRY._serialized_options = b'8\001'
  _globals['_KLABDATA']._serialized_start=63
  _globals['_KLABDATA']._serialized_end=1619
  _globals['_KLABDATA_NOTIFICATION']._serialized_start=391
  _globals['_KLABDATA_NOTIFICATION']._serialized_end=500
  _globals['_KLABDATA_OBJECT']._serialized_start=503
  _globals['_KLABDATA_OBJECT']._serialized_end=987
  _globals['_KLABDATA_OBJECT_PROPERTIESENTRY']._serialized_start=889
  _globals['_KLABDATA_OBJECT_PROPERTIESENTRY']._serialized_end=938
  _globals['_KLABDATA_OBJECT_METADATAENTRY']._serialized_start=940
  _globals['_KLABDATA_OBJECT_METADATAENTRY']._serialized_end=987
  _globals['_KLABDATA_LOOKUPTABLE']._serialized_start=990
  _globals['_KLABDATA_LOOKUPTABLE']._serialized_end=1141
  _globals['_KLABDATA_LOOKUPTABLE_TABLEENTRY']._serialized_start=1097
  _globals['_KLABDATA_LOOKUPTABLE_TABLEENTRY']._serialized_end=1141
  _globals['_KLABDATA_STATE']._serialized_start=1144
  _globals['_KLABDATA_STATE']._serialized_end=1562
  _globals['_KLABDATA_STATE_METADATAENTRY']._serialized_start=940
  _globals['_KLABDATA_STATE_METADATAENTRY']._serialized_end=987
  _globals['_KLABDATA_SEVERITY']._serialized_start=1564
  _globals['_KLABDATA_SEVERITY']._serialized_end=1619
# @@protoc_insertion_point(module_scope)