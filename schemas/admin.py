from datetime import date
from pydantic import BaseModel


class AdminInfoOutput(BaseModel):
    id: int
    name: str
    login_time: date
    avatar: str
    introduction: str
    roles: list

    class Config:
        orm_mode = True


class ChangePwdInput(BaseModel):
    Password: str

# def BindValidParam():