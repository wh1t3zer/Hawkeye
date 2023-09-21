# 公共模型 删除/查询ID
from pydantic import BaseModel


class PublicIDInput(BaseModel):
    ID: int


# 校验新增参数，绑定结构体，校验参数


# 分页查询公共模型
class PublicListInput(BaseModel):
    Info: str
    Page: int
    Limit: int

    class Config:
        orm_mode = True
