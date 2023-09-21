import base64
import utils
import datetime
from fastapi import Request

from middleware.response import ResponseError
from utils.redis import redis_conn
from utils.const import AdminSessionInfoKey


def SessionAuthMiddleware(request: Request):
    session = eval(base64.b64decode(redis_conn.get(name="Admin").encode('utf-8')))
    user_info = eval(base64.b64decode(request.session.get('user').encode('utf-8')))
    if user_info is None or user_info != session:
        ResponseError(request, 500, "user not login")
        return


if __name__ == '__main__':
    SessionAuthMiddleware()
