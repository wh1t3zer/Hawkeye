# from fastapi import FastAPI, Request
# import trace
# SuccessCode: int = 0
# UndefErrorCode: int = 0
# ValidErrorCode: int = 0
# InternalErrorCode: int = 0
#
# #1000以下为通用码，1000以上为用户自定义码
# InvalidRequestErrorCode = 401
# CustomizeCode = 1000
#
# GroupAllSaveFlowError = 2001
#
import traceback
import trace

import contextvars
import uuid
from fastapi import FastAPI, Request


class ResponseCode:
    pass

class Response:
    ErrorCode: ResponseCode
    ErrorMsg: str
    Data: str
    TraceID: str
    Stack: str


request_id_context = contextvars.ContextVar('request-id')
async def add_request_id_header(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request_id_context.set(request_id)
    response = await call_next(request)
    response.headers["X-Request-Id"] = request_id
    request_id_context.set(None)
    return response

