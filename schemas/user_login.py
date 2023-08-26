from datetime import datetime
from pydantic import BaseModel


class UserSessionInfo(BaseModel):
    id: int
    user_name: str
    login_time: datetime

class UserLoginInput(BaseModel):
    user_name: str
    password: str

    class Config:
        orm_mode = True

class UserLoginOut(BaseModel):
    user_name: str

    class Config:
        orm_mode = True

class UserLoginOutput(BaseModel):
    Token: str


# def BindValidParam():



