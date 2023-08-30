import jsonmarshal
from fastapi import APIRouter
from jsonmarshal import unmarshal
import datetime

import utils.const
from utils.Redis import redis_conn
import schemas.admin_login

router = APIRouter(prefix='/admin')

# AdminInfo godoc
# @Summary 管理员信息
# @Description 管理员信息
# @Tags 管理员接口
# @ID /admin/admin_info
# @Accept  json
# @Produce  json
# @Success 200 {object} middleware.Response{data=AdminInfoOutput} "success"
# @Router /admin/admin_info [get]
@router.get('/admin_info')
def admin_info():
    tmp = redis_conn.get(name=utils.const.AdminSessionInfoKey)
    sessInfo = unmarshal(bytes(tmp.encode()),schema="")
    print(sessInfo)
    userSessionInfo = schemas.admin_login.UserSessionInfo()

@router.post('/change_pwd')
def change_pwd():
    return 1