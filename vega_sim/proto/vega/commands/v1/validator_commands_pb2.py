# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vega/commands/v1/validator_commands.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ... import vega_pb2 as vega_dot_vega__pb2
from ... import chain_events_pb2 as vega_dot_chain__events__pb2
from ...commands.v1 import signature_pb2 as vega_dot_commands_dot_v1_dot_signature__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n)vega/commands/v1/validator_commands.proto\x12\x10vega.commands.v1\x1a\x0fvega/vega.proto\x1a\x17vega/chain_events.proto\x1a vega/commands/v1/signature.proto"\xbd\x01\n\x12ValidatorHeartbeat\x12\x17\n\x07node_id\x18\x01 \x01(\tR\x06nodeId\x12J\n\x12\x65thereum_signature\x18\x02 \x01(\x0b\x32\x1b.vega.commands.v1.SignatureR\x11\x65thereumSignature\x12\x42\n\x0evega_signature\x18\x03 \x01(\x0b\x32\x1b.vega.commands.v1.SignatureR\rvegaSignature"\x80\x04\n\x0c\x41nnounceNode\x12 \n\x0cvega_pub_key\x18\x01 \x01(\tR\nvegaPubKey\x12)\n\x10\x65thereum_address\x18\x02 \x01(\tR\x0f\x65thereumAddress\x12"\n\rchain_pub_key\x18\x03 \x01(\tR\x0b\x63hainPubKey\x12\x19\n\x08info_url\x18\x04 \x01(\tR\x07infoUrl\x12\x18\n\x07\x63ountry\x18\x05 \x01(\tR\x07\x63ountry\x12\x0e\n\x02id\x18\x06 \x01(\tR\x02id\x12\x12\n\x04name\x18\x07 \x01(\tR\x04name\x12\x1d\n\navatar_url\x18\x08 \x01(\tR\tavatarUrl\x12+\n\x12vega_pub_key_index\x18\t \x01(\rR\x0fvegaPubKeyIndex\x12\x1d\n\nfrom_epoch\x18\n \x01(\x04R\tfromEpoch\x12J\n\x12\x65thereum_signature\x18\x0b \x01(\x0b\x32\x1b.vega.commands.v1.SignatureR\x11\x65thereumSignature\x12\x42\n\x0evega_signature\x18\x0c \x01(\x0b\x32\x1b.vega.commands.v1.SignatureR\rvegaSignature\x12+\n\x11submitter_address\x18\r \x01(\tR\x10submitterAddress"\xc0\x03\n\x08NodeVote\x12\x1c\n\treference\x18\x02 \x01(\tR\treference\x12\x33\n\x04type\x18\x03 \x01(\x0e\x32\x1f.vega.commands.v1.NodeVote.TypeR\x04type"\xda\x02\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14TYPE_STAKE_DEPOSITED\x10\x01\x12\x16\n\x12TYPE_STAKE_REMOVED\x10\x02\x12\x18\n\x14TYPE_FUNDS_DEPOSITED\x10\x03\x12\x15\n\x11TYPE_SIGNER_ADDED\x10\x04\x12\x17\n\x13TYPE_SIGNER_REMOVED\x10\x05\x12\x17\n\x13TYPE_BRIDGE_STOPPED\x10\x06\x12\x17\n\x13TYPE_BRIDGE_RESUMED\x10\x07\x12\x15\n\x11TYPE_ASSET_LISTED\x10\x08\x12\x17\n\x13TYPE_LIMITS_UPDATED\x10\t\x12\x1b\n\x17TYPE_STAKE_TOTAL_SUPPLY\x10\n\x12\x1d\n\x19TYPE_SIGNER_THRESHOLD_SET\x10\x0b\x12"\n\x1eTYPE_GOVERNANCE_VALIDATE_ASSET\x10\x0cJ\x04\x08\x01\x10\x02"j\n\rNodeSignature\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x10\n\x03sig\x18\x02 \x01(\x0cR\x03sig\x12\x37\n\x04kind\x18\x03 \x01(\x0e\x32#.vega.commands.v1.NodeSignatureKindR\x04kind"\xb1\x02\n\nChainEvent\x12\x13\n\x05tx_id\x18\x01 \x01(\tR\x04txId\x12\x14\n\x05nonce\x18\x02 \x01(\x04R\x05nonce\x12\x34\n\x07\x62uiltin\x18\xe9\x07 \x01(\x0b\x32\x17.vega.BuiltinAssetEventH\x00R\x07\x62uiltin\x12)\n\x05\x65rc20\x18\xea\x07 \x01(\x0b\x32\x10.vega.ERC20EventH\x00R\x05\x65rc20\x12:\n\rstaking_event\x18\xed\x07 \x01(\x0b\x32\x12.vega.StakingEventH\x00R\x0cstakingEvent\x12\x42\n\x0e\x65rc20_multisig\x18\xee\x07 \x01(\x0b\x32\x18.vega.ERC20MultiSigEventH\x00R\rerc20MultisigB\x07\n\x05\x65ventJ\x06\x08\xeb\x07\x10\xec\x07J\x06\x08\xec\x07\x10\xed\x07"\xb4\x01\n\x13KeyRotateSubmission\x12)\n\x11new_pub_key_index\x18\x01 \x01(\rR\x0enewPubKeyIndex\x12!\n\x0ctarget_block\x18\x02 \x01(\x04R\x0btargetBlock\x12\x1e\n\x0bnew_pub_key\x18\x03 \x01(\tR\tnewPubKey\x12/\n\x14\x63urrent_pub_key_hash\x18\x04 \x01(\tR\x11\x63urrentPubKeyHash"\x83\x02\n\x1b\x45thereumKeyRotateSubmission\x12!\n\x0ctarget_block\x18\x01 \x01(\x04R\x0btargetBlock\x12\x1f\n\x0bnew_address\x18\x02 \x01(\tR\nnewAddress\x12\'\n\x0f\x63urrent_address\x18\x03 \x01(\tR\x0e\x63urrentAddress\x12+\n\x11submitter_address\x18\x04 \x01(\tR\x10submitterAddress\x12J\n\x12\x65thereum_signature\x18\x05 \x01(\x0b\x32\x1b.vega.commands.v1.SignatureR\x11\x65thereumSignature"M\n\x15StateVariableProposal\x12\x34\n\x08proposal\x18\x01 \x01(\x0b\x32\x18.vega.StateValueProposalR\x08proposal"u\n\x17ProtocolUpgradeProposal\x12\x30\n\x14upgrade_block_height\x18\x01 \x01(\x04R\x12upgradeBlockHeight\x12(\n\x10vega_release_tag\x18\x02 \x01(\tR\x0evegaReleaseTag"\x94\x01\n\x0fIssueSignatures\x12\x1c\n\tsubmitter\x18\x01 \x01(\tR\tsubmitter\x12\x37\n\x04kind\x18\x02 \x01(\x0e\x32#.vega.commands.v1.NodeSignatureKindR\x04kind\x12*\n\x11validator_node_id\x18\x03 \x01(\tR\x0fvalidatorNodeId*\x97\x02\n\x11NodeSignatureKind\x12#\n\x1fNODE_SIGNATURE_KIND_UNSPECIFIED\x10\x00\x12!\n\x1dNODE_SIGNATURE_KIND_ASSET_NEW\x10\x01\x12(\n$NODE_SIGNATURE_KIND_ASSET_WITHDRAWAL\x10\x02\x12\x33\n/NODE_SIGNATURE_KIND_ERC20_MULTISIG_SIGNER_ADDED\x10\x03\x12\x35\n1NODE_SIGNATURE_KIND_ERC20_MULTISIG_SIGNER_REMOVED\x10\x04\x12$\n NODE_SIGNATURE_KIND_ASSET_UPDATE\x10\x05\x42\x33Z1code.vegaprotocol.io/vega/protos/vega/commands/v1b\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "vega.commands.v1.validator_commands_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"Z1code.vegaprotocol.io/vega/protos/vega/commands/v1"
    )
    _NODESIGNATUREKIND._serialized_start = 2508
    _NODESIGNATUREKIND._serialized_end = 2787
    _VALIDATORHEARTBEAT._serialized_start = 140
    _VALIDATORHEARTBEAT._serialized_end = 329
    _ANNOUNCENODE._serialized_start = 332
    _ANNOUNCENODE._serialized_end = 844
    _NODEVOTE._serialized_start = 847
    _NODEVOTE._serialized_end = 1295
    _NODEVOTE_TYPE._serialized_start = 943
    _NODEVOTE_TYPE._serialized_end = 1289
    _NODESIGNATURE._serialized_start = 1297
    _NODESIGNATURE._serialized_end = 1403
    _CHAINEVENT._serialized_start = 1406
    _CHAINEVENT._serialized_end = 1711
    _KEYROTATESUBMISSION._serialized_start = 1714
    _KEYROTATESUBMISSION._serialized_end = 1894
    _ETHEREUMKEYROTATESUBMISSION._serialized_start = 1897
    _ETHEREUMKEYROTATESUBMISSION._serialized_end = 2156
    _STATEVARIABLEPROPOSAL._serialized_start = 2158
    _STATEVARIABLEPROPOSAL._serialized_end = 2235
    _PROTOCOLUPGRADEPROPOSAL._serialized_start = 2237
    _PROTOCOLUPGRADEPROPOSAL._serialized_end = 2354
    _ISSUESIGNATURES._serialized_start = 2357
    _ISSUESIGNATURES._serialized_end = 2505
# @@protoc_insertion_point(module_scope)
