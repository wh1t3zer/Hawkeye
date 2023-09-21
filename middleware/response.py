import pickle

import jsonmarshal
from fastapi import Request
from pydantic import BaseModel


class ResponseCode(BaseModel):
    ErrorCode: int

    # pass
    class Config:
        orm_mode = True


class Response(BaseModel):
    ErrorCode: int
    ErrorMsg: str
    Data: str
    TraceID: str

    # Stack: str

    class Config:
        orm_mode = True


SuccessCode: ResponseCode = 0
UndefErrorCode: ResponseCode = 1
ValidErrorCode: ResponseCode = 2
InternalErrorCode: ResponseCode = 3

# 1000以下为通用码，1000以上为用户自定义码
InvalidRequestErrorCode: ResponseCode = 401
CustomizeCode: ResponseCode = 1000
GroupAllSaveFlowError: ResponseCode = 2001


def ResponseError(request: Request, code: ResponseCode, err):
    global TraceID
    context = request.state.context
    if context:
        TraceID = context.request_id
    resp = Response(ErrorCode=code, ErrorMsg=err, Data="", TraceID=TraceID)
    request.state.__setattr__("response", resp)


def ResponseSuccess(request: Request, data):
    global TraceID
    context = request.state.context
    if context:
        TraceID = context.request_id
    resp = Response(ErrorCode=SuccessCode, Data=data, ErrorMsg="", TraceID=TraceID)
    request.state.__setattr__("response", resp)
