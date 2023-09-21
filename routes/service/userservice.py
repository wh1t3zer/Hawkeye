from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, Response

import models.user
import utils.code
from models.user import User


def check_user(db: Session, user: User):
    db_user = models.user.FindByName(user, db)
    if db_user is None:
        # raise HTTPException(status_code=400, detail="用户信息不存在")
        return JSONResponse(
            content=jsonable_encoder({"error": "用户信息不存在"})
        ), None
    else:
        saltPassword = utils.code.GenSaltPassword(user.password, 'admin')
        if saltPassword != db_user.password:
            # raise HTTPException(status_code=400, detail="密码错误，请重新输入")
            return JSONResponse(
                content={"error": "账号或密码错误，请重新输入"}
            ), None
        else:
            return None, db_user
