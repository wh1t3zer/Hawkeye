import datetime

from fastapi import APIRouter, FastAPI,status
from fastapi import Depends
from jsonmarshal import marshal
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware

import utils.const
from middleware.response import response
from routes.service.userservice import check_user
import schemas.user_login
from utils.database import get_db

router = APIRouter()
app = FastAPI()
app.add_middleware(SessionMiddleware,secret_key="secret")


# @Summary 管理员登陆
# @Description 管理员登陆
# @Tags 管理员接口
# @ID /login
# @Accept  json
# @Produce  json
# @Success 200 {object} middleware.Response{data=dto.AdminLoginOutput} "success"
# @Router /login [post]
@router.post('/login',response_model=schemas.user_login.UserLoginInfo)
def login(user: schemas.user_login.UserLoginInput, db: Session = Depends(get_db)):
    user_info = check_user(db, user)


    # 设置session
    ID = user_info.id
    username = user_info.user_name
    login_time = datetime.datetime.now()
    sessInfo = schemas.user_login.UserSessionInfo(ID, username, login_time)
    admin_info = marshal(sessInfo.__dict__)
    Token = user_info.user_name
    import logging
    logger = logging.getLogger()

    formatter = logging.Formatter(
        "%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s"
    )
    logger.critical("call")
    logger.error("call")
    logger.warning("call")
    logger.info("call")
    logger.debug("call")
    to_console = logging.StreamHandler()
    to_console.setFormatter(formatter)
    logger.addHandler(to_console)
    return user_info


@router.get('/logout')
async def logout():
    return response(content={"haha":"haha"},msg={"data":"test"},error=None,status=status.HTTP_200_OK)
