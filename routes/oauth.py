from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import models.user



#Oauth验证
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