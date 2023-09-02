import datetime
import pickle
import base64
from fastapi import APIRouter, FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware
import utils.const
from middleware.response import response
from routes.service.userservice import check_user
import schemas.admin_login
from utils.database import get_db
from utils.Redis import redis_conn

app = FastAPI()
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
async def login(user: schemas.admin_login.UserLoginInput, db: Session = Depends(get_db)):
    user_info = check_user(db, user)
    # 设置session
    if user_info is not None:
        sessInfo = schemas.admin_login.UserSessionInfo(
            id=user_info.id,
            user_name=user_info.user_name,
            login_time=datetime.datetime.now()
        )
        sess_info = pickle.dumps(sessInfo.__dict__)
        key = utils.const.AdminSessionInfoKey
        # 将session存到redis,pickle与redis特殊性 b64
        redis_conn.set(name=key, value=base64.b64encode(sess_info))
        redis_conn.save()
        Token = user_info.user_name
        return user_info
    else:
        return "error"


@router.get('/logout')
async def logout():
    # 直接清空redis session缓存
    redis_conn.delete(utils.const.AdminSessionInfoKey)
    redis_conn.save()
    return "Logout Successfully!"
