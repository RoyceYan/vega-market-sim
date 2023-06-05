# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blockexplorer/api/v1/blockexplorer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from vega.commands.v1 import signature_pb2 as vega_dot_commands_dot_v1_dot_signature__pb2
from vega.commands.v1 import transaction_pb2 as vega_dot_commands_dot_v1_dot_transaction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(blockexplorer/api/v1/blockexplorer.proto\x12\x14\x62lockexplorer.api.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a vega/commands/v1/signature.proto\x1a\"vega/commands/v1/transaction.proto\"\r\n\x0bInfoRequest\"I\n\x0cInfoResponse\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12\x1f\n\x0b\x63ommit_hash\x18\x02 \x01(\tR\ncommitHash\"0\n\x15GetTransactionRequest\x12\x17\n\x04hash\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x04hash\"]\n\x16GetTransactionResponse\x12\x43\n\x0btransaction\x18\x01 \x01(\x0b\x32!.blockexplorer.api.v1.TransactionR\x0btransaction\"\x8e\x02\n\x17ListTransactionsRequest\x12\x14\n\x05limit\x18\x01 \x01(\rR\x05limit\x12\x1b\n\x06\x62\x65\x66ore\x18\x02 \x01(\tH\x00R\x06\x62\x65\x66ore\x88\x01\x01\x12\x19\n\x05\x61\x66ter\x18\x03 \x01(\tH\x01R\x05\x61\x66ter\x88\x01\x01\x12T\n\x07\x66ilters\x18\x04 \x03(\x0b\x32:.blockexplorer.api.v1.ListTransactionsRequest.FiltersEntryR\x07\x66ilters\x1a:\n\x0c\x46iltersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\t\n\x07_beforeB\x08\n\x06_after\"a\n\x18ListTransactionsResponse\x12\x45\n\x0ctransactions\x18\x03 \x03(\x0b\x32!.blockexplorer.api.v1.TransactionR\x0ctransactions\"\xc2\x02\n\x0bTransaction\x12\x14\n\x05\x62lock\x18\x01 \x01(\x04R\x05\x62lock\x12\x14\n\x05index\x18\x02 \x01(\rR\x05index\x12\x12\n\x04hash\x18\x03 \x01(\tR\x04hash\x12\x1c\n\tsubmitter\x18\x04 \x01(\tR\tsubmitter\x12\x12\n\x04type\x18\x05 \x01(\tR\x04type\x12\x12\n\x04\x63ode\x18\x06 \x01(\rR\x04\x63ode\x12\x16\n\x06\x63ursor\x18\x07 \x01(\tR\x06\x63ursor\x12\x35\n\x07\x63ommand\x18\x08 \x01(\x0b\x32\x1b.vega.commands.v1.InputDataR\x07\x63ommand\x12\x39\n\tsignature\x18\t \x01(\x0b\x32\x1b.vega.commands.v1.SignatureR\tsignature\x12\x19\n\x05\x65rror\x18\n \x01(\tH\x00R\x05\x65rror\x88\x01\x01\x42\x08\n\x06_error2\xc9\x02\n\x14\x42lockExplorerService\x12m\n\x0eGetTransaction\x12+.blockexplorer.api.v1.GetTransactionRequest\x1a,.blockexplorer.api.v1.GetTransactionResponse\"\x00\x12s\n\x10ListTransactions\x12-.blockexplorer.api.v1.ListTransactionsRequest\x1a..blockexplorer.api.v1.ListTransactionsResponse\"\x00\x12M\n\x04Info\x12!.blockexplorer.api.v1.InfoRequest\x1a\".blockexplorer.api.v1.InfoResponseBxZ5code.vegaprotocol.io/vega/protos/blockexplorer/api/v1\x92\x41>\x12#\n\x18Vega block explorer APIs2\x07v0.71.0\x1a\x13lb.testnet.vega.xyz*\x02\x01\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'blockexplorer.api.v1.blockexplorer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5code.vegaprotocol.io/vega/protos/blockexplorer/api/v1\222A>\022#\n\030Vega block explorer APIs2\007v0.71.0\032\023lb.testnet.vega.xyz*\002\001\002'
  _GETTRANSACTIONREQUEST.fields_by_name['hash']._options = None
  _GETTRANSACTIONREQUEST.fields_by_name['hash']._serialized_options = b'\340A\002'
  _LISTTRANSACTIONSREQUEST_FILTERSENTRY._options = None
  _LISTTRANSACTIONSREQUEST_FILTERSENTRY._serialized_options = b'8\001'
  _INFOREQUEST._serialized_start=217
  _INFOREQUEST._serialized_end=230
  _INFORESPONSE._serialized_start=232
  _INFORESPONSE._serialized_end=305
  _GETTRANSACTIONREQUEST._serialized_start=307
  _GETTRANSACTIONREQUEST._serialized_end=355
  _GETTRANSACTIONRESPONSE._serialized_start=357
  _GETTRANSACTIONRESPONSE._serialized_end=450
  _LISTTRANSACTIONSREQUEST._serialized_start=453
  _LISTTRANSACTIONSREQUEST._serialized_end=723
  _LISTTRANSACTIONSREQUEST_FILTERSENTRY._serialized_start=644
  _LISTTRANSACTIONSREQUEST_FILTERSENTRY._serialized_end=702
  _LISTTRANSACTIONSRESPONSE._serialized_start=725
  _LISTTRANSACTIONSRESPONSE._serialized_end=822
  _TRANSACTION._serialized_start=825
  _TRANSACTION._serialized_end=1147
  _BLOCKEXPLORERSERVICE._serialized_start=1150
  _BLOCKEXPLORERSERVICE._serialized_end=1479
# @@protoc_insertion_point(module_scope)
