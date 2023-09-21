from datetime import datetime

from pydantic import BaseModel, validator


class UserLoginInput(BaseModel):
    user_name: str
    password: str


class UserLoginInfo(BaseModel):
    id: int
    user_name: str
    # is_delete: int

    class Config:
        orm_mode = True


class UserLoginOutput(BaseModel):
    Token: str


class UserSessionInfo:
    def __init__(self, id, user_name, login_time):
        self.id = id
        self.user_name = user_name
        self.login_time = login_time


# def BindValidParam():
