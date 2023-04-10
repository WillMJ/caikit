# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model-runtime.proto
"""Generated protocol buffer code."""
# Third Party
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13model-runtime.proto\x12\x05mmesh"[\n\x10LoadModelRequest\x12\x0f\n\x07modelId\x18\x01 \x01(\t\x12\x11\n\tmodelType\x18\x02 \x01(\t\x12\x11\n\tmodelPath\x18\x03 \x01(\t\x12\x10\n\x08modelKey\x18\x04 \x01(\t"@\n\x11LoadModelResponse\x12\x13\n\x0bsizeInBytes\x18\x01 \x01(\x04\x12\x16\n\x0emaxConcurrency\x18\x02 \x01(\r"%\n\x12UnloadModelRequest\x12\x0f\n\x07modelId\x18\x01 \x01(\t"\x15\n\x13UnloadModelResponse"b\n\x17PredictModelSizeRequest\x12\x0f\n\x07modelId\x18\x01 \x01(\t\x12\x11\n\tmodelType\x18\x02 \x01(\t\x12\x11\n\tmodelPath\x18\x03 \x01(\t\x12\x10\n\x08modelKey\x18\x04 \x01(\t"/\n\x18PredictModelSizeResponse\x12\x13\n\x0bsizeInBytes\x18\x01 \x01(\x04"#\n\x10ModelSizeRequest\x12\x0f\n\x07modelId\x18\x01 \x01(\t"(\n\x11ModelSizeResponse\x12\x13\n\x0bsizeInBytes\x18\x01 \x01(\x04"\x16\n\x14RuntimeStatusRequest"\xaa\x04\n\x15RuntimeStatusResponse\x12\x33\n\x06status\x18\x01 \x01(\x0e\x32#.mmesh.RuntimeStatusResponse.Status\x12\x17\n\x0f\x63\x61pacityInBytes\x18\x02 \x01(\x04\x12\x1d\n\x15maxLoadingConcurrency\x18\x03 \x01(\r\x12\x1d\n\x15modelLoadingTimeoutMs\x18\x04 \x01(\r\x12\x1f\n\x17\x64\x65\x66\x61ultModelSizeInBytes\x18\x05 \x01(\x04\x12\x16\n\x0eruntimeVersion\x18\x06 \x01(\t\x12\x1d\n\x15numericRuntimeVersion\x18\x07 \x01(\x04\x12\x42\n\x0bmethodInfos\x18\x08 \x03(\x0b\x32-.mmesh.RuntimeStatusResponse.MethodInfosEntry\x12\x1d\n\x15limitModelConcurrency\x18\t \x01(\x08\x12\x16\n\x0e\x61llowAnyMethod\x18\n \x01(\x08\x1a%\n\nMethodInfo\x12\x17\n\x0fidInjectionPath\x18\x01 \x03(\r\x1a[\n\x10MethodInfosEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.mmesh.RuntimeStatusResponse.MethodInfo:\x02\x38\x01".\n\x06Status\x12\x0c\n\x08STARTING\x10\x00\x12\t\n\x05READY\x10\x01\x12\x0b\n\x07\x46\x41ILING\x10\x02\x32\xff\x02\n\x0cModelRuntime\x12@\n\tloadModel\x12\x17.mmesh.LoadModelRequest\x1a\x18.mmesh.LoadModelResponse"\x00\x12\x46\n\x0bunloadModel\x12\x19.mmesh.UnloadModelRequest\x1a\x1a.mmesh.UnloadModelResponse"\x00\x12U\n\x10predictModelSize\x12\x1e.mmesh.PredictModelSizeRequest\x1a\x1f.mmesh.PredictModelSizeResponse"\x00\x12@\n\tmodelSize\x12\x17.mmesh.ModelSizeRequest\x1a\x18.mmesh.ModelSizeResponse"\x00\x12L\n\rruntimeStatus\x12\x1b.mmesh.RuntimeStatusRequest\x1a\x1c.mmesh.RuntimeStatusResponse"\x00\x42 \n\x1c\x63om.ibm.watson.modelmesh.apiP\x01\x62\x06proto3'
)


_LOADMODELREQUEST = DESCRIPTOR.message_types_by_name["LoadModelRequest"]
_LOADMODELRESPONSE = DESCRIPTOR.message_types_by_name["LoadModelResponse"]
_UNLOADMODELREQUEST = DESCRIPTOR.message_types_by_name["UnloadModelRequest"]
_UNLOADMODELRESPONSE = DESCRIPTOR.message_types_by_name["UnloadModelResponse"]
_PREDICTMODELSIZEREQUEST = DESCRIPTOR.message_types_by_name["PredictModelSizeRequest"]
_PREDICTMODELSIZERESPONSE = DESCRIPTOR.message_types_by_name["PredictModelSizeResponse"]
_MODELSIZEREQUEST = DESCRIPTOR.message_types_by_name["ModelSizeRequest"]
_MODELSIZERESPONSE = DESCRIPTOR.message_types_by_name["ModelSizeResponse"]
_RUNTIMESTATUSREQUEST = DESCRIPTOR.message_types_by_name["RuntimeStatusRequest"]
_RUNTIMESTATUSRESPONSE = DESCRIPTOR.message_types_by_name["RuntimeStatusResponse"]
_RUNTIMESTATUSRESPONSE_METHODINFO = _RUNTIMESTATUSRESPONSE.nested_types_by_name[
    "MethodInfo"
]
_RUNTIMESTATUSRESPONSE_METHODINFOSENTRY = _RUNTIMESTATUSRESPONSE.nested_types_by_name[
    "MethodInfosEntry"
]
_RUNTIMESTATUSRESPONSE_STATUS = _RUNTIMESTATUSRESPONSE.enum_types_by_name["Status"]
LoadModelRequest = _reflection.GeneratedProtocolMessageType(
    "LoadModelRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOADMODELREQUEST,
        "__module__": "model_runtime_pb2"
        # @@protoc_insertion_point(class_scope:mmesh.LoadModelRequest)
    },
)
_sym_db.RegisterMessage(LoadModelRequest)

LoadModelResponse = _reflection.GeneratedProtocolMessageType(
    "LoadModelResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOADMODELRESPONSE,
        "__module__": "model_runtime_pb2"
        # @@protoc_insertion_point(class_scope:mmesh.LoadModelResponse)
    },
)
_sym_db.RegisterMessage(LoadModelResponse)

UnloadModelRequest = _reflection.GeneratedProtocolMessageType(
    "UnloadModelRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UNLOADMODELREQUEST,
        "__module__": "model_runtime_pb2"
        # @@protoc_insertion_point(class_scope:mmesh.UnloadModelRequest)
    },
)
_sym_db.RegisterMessage(UnloadModelRequest)

UnloadModelResponse = _reflection.GeneratedProtocolMessageType(
    "UnloadModelResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UNLOADMODELRESPONSE,
        "__module__": "model_runtime_pb2"
        # @@protoc_insertion_point(class_scope:mmesh.UnloadModelResponse)
    },
)
_sym_db.RegisterMessage(UnloadModelResponse)

PredictModelSizeRequest = _reflection.GeneratedProtocolMessageType(
    "PredictModelSizeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _PREDICTMODELSIZEREQUEST,
        "__module__": "model_runtime_pb2"
        # @@protoc_insertion_point(class_scope:mmesh.PredictModelSizeRequest)
    },
)
_sym_db.RegisterMessage(PredictModelSizeRequest)

PredictModelSizeResponse = _reflection.GeneratedProtocolMessageType(
    "PredictModelSizeResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _PREDICTMODELSIZERESPONSE,
        "__module__": "model_runtime_pb2"
        # @@protoc_insertion_point(class_scope:mmesh.PredictModelSizeResponse)
    },
)
_sym_db.RegisterMessage(PredictModelSizeResponse)

ModelSizeRequest = _reflection.GeneratedProtocolMessageType(
    "ModelSizeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _MODELSIZEREQUEST,
        "__module__": "model_runtime_pb2"
        # @@protoc_insertion_point(class_scope:mmesh.ModelSizeRequest)
    },
)
_sym_db.RegisterMessage(ModelSizeRequest)

ModelSizeResponse = _reflection.GeneratedProtocolMessageType(
    "ModelSizeResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MODELSIZERESPONSE,
        "__module__": "model_runtime_pb2"
        # @@protoc_insertion_point(class_scope:mmesh.ModelSizeResponse)
    },
)
_sym_db.RegisterMessage(ModelSizeResponse)

RuntimeStatusRequest = _reflection.GeneratedProtocolMessageType(
    "RuntimeStatusRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _RUNTIMESTATUSREQUEST,
        "__module__": "model_runtime_pb2"
        # @@protoc_insertion_point(class_scope:mmesh.RuntimeStatusRequest)
    },
)
_sym_db.RegisterMessage(RuntimeStatusRequest)

RuntimeStatusResponse = _reflection.GeneratedProtocolMessageType(
    "RuntimeStatusResponse",
    (_message.Message,),
    {
        "MethodInfo": _reflection.GeneratedProtocolMessageType(
            "MethodInfo",
            (_message.Message,),
            {
                "DESCRIPTOR": _RUNTIMESTATUSRESPONSE_METHODINFO,
                "__module__": "model_runtime_pb2"
                # @@protoc_insertion_point(class_scope:mmesh.RuntimeStatusResponse.MethodInfo)
            },
        ),
        "MethodInfosEntry": _reflection.GeneratedProtocolMessageType(
            "MethodInfosEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _RUNTIMESTATUSRESPONSE_METHODINFOSENTRY,
                "__module__": "model_runtime_pb2"
                # @@protoc_insertion_point(class_scope:mmesh.RuntimeStatusResponse.MethodInfosEntry)
            },
        ),
        "DESCRIPTOR": _RUNTIMESTATUSRESPONSE,
        "__module__": "model_runtime_pb2"
        # @@protoc_insertion_point(class_scope:mmesh.RuntimeStatusResponse)
    },
)
_sym_db.RegisterMessage(RuntimeStatusResponse)
_sym_db.RegisterMessage(RuntimeStatusResponse.MethodInfo)
_sym_db.RegisterMessage(RuntimeStatusResponse.MethodInfosEntry)

_MODELRUNTIME = DESCRIPTOR.services_by_name["ModelRuntime"]
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\034com.ibm.watson.modelmesh.apiP\001"
    _RUNTIMESTATUSRESPONSE_METHODINFOSENTRY._options = None
    _RUNTIMESTATUSRESPONSE_METHODINFOSENTRY._serialized_options = b"8\001"
    _LOADMODELREQUEST._serialized_start = 30
    _LOADMODELREQUEST._serialized_end = 121
    _LOADMODELRESPONSE._serialized_start = 123
    _LOADMODELRESPONSE._serialized_end = 187
    _UNLOADMODELREQUEST._serialized_start = 189
    _UNLOADMODELREQUEST._serialized_end = 226
    _UNLOADMODELRESPONSE._serialized_start = 228
    _UNLOADMODELRESPONSE._serialized_end = 249
    _PREDICTMODELSIZEREQUEST._serialized_start = 251
    _PREDICTMODELSIZEREQUEST._serialized_end = 349
    _PREDICTMODELSIZERESPONSE._serialized_start = 351
    _PREDICTMODELSIZERESPONSE._serialized_end = 398
    _MODELSIZEREQUEST._serialized_start = 400
    _MODELSIZEREQUEST._serialized_end = 435
    _MODELSIZERESPONSE._serialized_start = 437
    _MODELSIZERESPONSE._serialized_end = 477
    _RUNTIMESTATUSREQUEST._serialized_start = 479
    _RUNTIMESTATUSREQUEST._serialized_end = 501
    _RUNTIMESTATUSRESPONSE._serialized_start = 504
    _RUNTIMESTATUSRESPONSE._serialized_end = 1058
    _RUNTIMESTATUSRESPONSE_METHODINFO._serialized_start = 880
    _RUNTIMESTATUSRESPONSE_METHODINFO._serialized_end = 917
    _RUNTIMESTATUSRESPONSE_METHODINFOSENTRY._serialized_start = 919
    _RUNTIMESTATUSRESPONSE_METHODINFOSENTRY._serialized_end = 1010
    _RUNTIMESTATUSRESPONSE_STATUS._serialized_start = 1012
    _RUNTIMESTATUSRESPONSE_STATUS._serialized_end = 1058
    _MODELRUNTIME._serialized_start = 1061
    _MODELRUNTIME._serialized_end = 1444
# @@protoc_insertion_point(module_scope)