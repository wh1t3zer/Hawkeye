from datetime import date
from pydantic import BaseModel


class AdminSessionInfo(BaseModel):
    id: int
    name: str
    login_time: date
    avatar: str
    introduction: str
    roles: list

class ChangePwdInput(BaseModel):
    Password: str

# def BindValidParam():