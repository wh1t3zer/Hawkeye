from fastapi import HTTPException, FastAPI
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware

import models.user
import utils.code
from models.user import User





app = FastAPI()


def check_user(db: Session, user: User):
    db_user = db.query(models.user.User).filter(models.user.User.user_name == user.user_name).first()
    if db_user is None:
        raise HTTPException(status_code=400, detail="用户信息不存在")
    else:
        saltPassword = utils.code.GenSaltPassword(user.password, 'admin')
        if saltPassword != db_user.password:
            raise HTTPException(status_code=400, detail=f"密码错误，请重新输入")
        else:
            return db_user
