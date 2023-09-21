import json
import pickle
import base64
from fastapi import APIRouter, FastAPI, Depends
from fastapi import Request
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import JSONResponse

import middleware.response
import utils.const
from middleware.response import ResponseSuccess
from middleware.session_auth import SessionAuthMiddleware
from routes.service.userservice import check_user
import schemas.admin_login
from utils.database import get_db
from utils.redis import redis_conn

from datetime import datetime

app = FastAPI()
router = APIRouter(prefix="/admin")


# @Summary 管理员登陆
# @Description 管理员登陆
# @Tags 管理员接口
# @ID /login
# @Accept  json
# @Produce  json
# @Success 200 {object} middleware.Response{data=user_info} "success"
# @Router /admin/login [post]
@router.post('/login', response_class=JSONResponse)
async def login(user: schemas.admin_login.UserLoginInput, request: Request, db: Session = Depends(get_db)):
    resp, user_info = check_user(db, user)
    if resp is not None:
        err = json.loads(resp.body)['error']
        middleware.response.ResponseError(request, 2002, err)
        return
    # 设置session
    elif user_info is not None:
        sessInfo = schemas.admin_login.UserSessionInfo(
            id=user_info.id,
            user_name=user_info.user_name,
            login_time=datetime.now()
        )
        # 序列化python对象到byte
        # sess_info = pickle.dumps(sessInfo.__dict__)
        sess_info = base64.b64encode(str(vars(sessInfo)).encode('utf-8')).decode('utf-8')
        # 写入session
        request.session.update({"user": sess_info})
        # 将session存到redis,pickle与redis特殊性 b64
        key = utils.const.AdminSessionInfoKey
        redis_conn.set(name=key, value=sess_info)
        # redis_conn.set(name=key, value=sess_info)
        redis_conn.save()
        Token = user_info.user_name
        middleware.response.ResponseSuccess(request, Token)


# AdminLoginOut godoc
# @Summary 管理员退出
# @Description 管理员退出
# @Tags 管理员接口
# @ID /admin_login/logout
# @Accept  json
# @Produce  json
# @Success 200 {object} middleware.Response{data=string} "success"
# @Router /admin/logout [get]
@router.get('/logout')
async def logout(request: Request):
    # 直接清空redis session缓存
    redis_conn.delete(utils.const.AdminSessionInfoKey)
    redis_conn.save()
    ResponseSuccess(request=request, data="Logout Successfully!")
