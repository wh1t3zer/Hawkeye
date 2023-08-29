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
from json import dumps

from fastapi.responses import Response


class response(Response):
    def __init__(self, content, msg, status,error=None):
        if msg:
            content['msg'] = msg
        if error:
            content['error'] = error
        super().__init__(
            content=dumps(content),
            media_type="application/json",
            status_code=status
        )

