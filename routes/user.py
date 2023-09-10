import datetime
import json
import pickle
import base64
from fastapi import APIRouter, FastAPI, Depends
from fastapi import Request
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware
import utils.const
from middleware.response import add_request_id_header
from routes.service.userservice import check_user
import schemas.admin_login
from utils.database import get_db
from utils.redis import redis_conn
from utils.logs import logger

app = FastAPI()
router = APIRouter(prefix="/admin")
app.add_middleware(SessionMiddleware, secret_key="secret")


# @Summary 管理员登陆
# @Description 管理员登陆
# @Tags 管理员接口
# @ID /login
# @Accept  json
# @Produce  json
# @Success 200 {object} middleware.Response{data=AdminLoginOutput} "success"
# @Router /login [post]
@router.post('/login', response_model=schemas.admin_login.UserLoginInfo)
@logger.catch
async def login(user: schemas.admin_login.UserLoginInput, request: Request, db: Session = Depends(get_db)):
    user_info = check_user(db, user)
    # 设置session
    if user_info is not None:
        sessInfo = schemas.admin_login.UserSessionInfo(
            id=user_info.id,
            user_name=user_info.user_name,
            login_time=datetime.datetime.now()
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
        return user_info
    else:
        return "error"


@router.get('/logout')
async def logout(request: Request):
    # 直接清空redis session缓存
    # redis_conn.delete(utils.const.AdminSessionInfoKey)
    # redis_conn.save()
    # return "Logout Successfully!"
    print(request.app.state.logger)
