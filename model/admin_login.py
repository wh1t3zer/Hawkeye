from datetime import date
from pydantic import BaseModel


class AdminSessionInfo(BaseModel):
    id: int
    user_name: str
    login_time: date

class AdminLoginInput(BaseModel):
    UserName: str
    Password: str

class AdminLoginOutput(BaseModel):
    Token: str


# def BindValidParam():


