from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

import models.user
from models.user import get_user
import schemas.user_login
from utils.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()
@router.post('/login')
def login(user: schemas.user_login.UserLoginInput, db: Session=Depends(get_db)):
    db_user = get_user(db,user)
    if db_user is None:
        raise HTTPException(status_code=400, detail=f"{user.user_name}不存在")
    else:
        if(db_user.password!=user.password):
            raise HTTPException(status_code=400, detail=f"密码错误")
        else:
            raise HTTPException(status_code=200, detail=f"success")



@router.get('/logout')
def logout():
    return exit