import datetime
import json
import pickle
import base64
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
import schemas.admin

import utils
from models.user import FindBySessionId, update
from schemas.admin import AdminInfoOutput
from utils.redis import redis_conn
from utils.code import GenSaltPassword
from utils.database import get_db

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
def admin_info(request: Request):
    # redis和session特性不同，字节类型错误
    # tmp = redis_conn.get(name=utils.const.AdminSessionInfoKey)
    # userSessionInfo = request.session.get('user')
    # user_info = pickle.loads(base64.b64decode(tmp))
    tmp = eval(base64.b64decode(redis_conn.get(name=utils.const.AdminSessionInfoKey).encode('utf-8')))
    userSessionInfo = eval(base64.b64decode(request.session.get('user').encode('utf-8')))
    # 判断是否为管理员
    if tmp == userSessionInfo:
        # pickle反序列化特殊性 b64
        # admin_info = pickle.loads(base64.b64decode(tmp))
        admin_info = userSessionInfo
        info = AdminInfoOutput(
            id=admin_info['id'],
            name=admin_info['user_name'],
            login_time=admin_info['login_time'],
            avatar="https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
            introduction="super administrator",
            roles=['admin']
        )
        return info
    else:
        return 'error'


# @Summary 修改密码
# @Description 修改密码
# @Tags 管理员接口
# @ID /admin/change_pwd
# @Accept  json
# @Produce  json
# @Param body body ChangePwdInput true "body"
# @Success 200 {object} middleware.Response{data=string} "success"
# @Router /admin/change_pwd [post]
@router.post('/change_pwd')
def change_pwd(admin: schemas.admin.ChangePwdInput, db: Session = Depends(get_db)):
    # 1.session读取用户信息到结构体 sessInfo
    # 2.sessInfo.ID 读取数据库信息 adminInfo
    # 3.sha256密码加盐 GenSaltPassword
    # 4.saltPassword == > adminInfo.password 执行数据保存
    sessInfo = pickle.loads(base64.b64decode(redis_conn.get(name=utils.const.AdminSessionInfoKey)))
    adminInfo = FindBySessionId(sessInfo, db)
    # 生成密码
    saltPassword = GenSaltPassword(admin.Password, adminInfo.salt)
    flag_change = update(saltPassword, adminInfo, db)
    if flag_change:
        return "success"
    else:
        return "error"
