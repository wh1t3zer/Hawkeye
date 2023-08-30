#Oauth验证
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

import models.user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#async def OauthRegister():

#def Tokens():


#def AdminLoginOut():
    # AdminLoginOut godoc
    #@Summary 管理员退出
    #@Description 管理员退出
    #@Tags 管理员接口
    #@ID / admin_login / logout
    #@Accept json
    #@Produce json
    #@Success 200 {object} middleware.Response {data = string} "success"
    #@Router / admin_login / logout[get]