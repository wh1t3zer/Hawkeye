import datetime

from fastapi import APIRouter, FastAPI, Request
from fastapi import Depends
from jsonmarshal import marshal
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware

import utils.const
from middleware.response import response
from routes.service.userservice import check_user
import schemas.admin_login
from utils.database import get_db
from utils.Redis import redis_conn

app =FastAPI()
router = APIRouter()
app.add_middleware(SessionMiddleware, secret_key="secret")


# @Summary 管理员登陆
# @Description 管理员登陆
# @Tags 管理员接口
# @ID /login
# @Accept  json
# @Produce  json
# @Success 200 {object} middleware.Response{data=AdminLoginOutput} "success" 中间件待开发
# @Router /login [post]
@router.post('/login', response_model=schemas.admin_login.UserLoginInfo)
async def login(user: schemas.admin_login.UserLoginInput, request: Request, db: Session = Depends(get_db)):
    user_info = check_user(db, user)
    # 设置session
    ID = user_info.id
    username = user_info.user_name
    login_time = datetime.datetime.now()
    sessInfo = schemas.admin_login.UserSessionInfo(ID, username, login_time)
    admin_info = marshal(sessInfo.__dict__)
    print(admin_info)
    key = utils.const.AdminSessionInfoKey
    #设置session
    redis_conn.set(name=key, value=str(admin_info))
    redis_conn.save()
    Token = user_info.user_name
    return user_info


@router.get('/logout')
async def logout():
    redis_conn.delete(utils.const.AdminSessionInfoKey)
    redis_conn.save()
    print(redis_conn.get(name=utils.const.AdminSessionInfoKey))
    return "Logout Successfully!"
