from pydantic import BaseModel
from typing import List


class TaskInfoOutput(BaseModel):
    ID: int
    RuleID: int
    Name: str
    TargetList: str
    WebScan: int
    PocScan: int
    AuthScan: int
    TrapScan: int
    Recursion: int
    Progress: str
    Percent: int
    Status: str
    CreatedAt: str
    UpdatedAt: str
    IsDelete: int
    AssetNum: int

    class Config:
        orm_mode = True


class TaskListOutput(BaseModel):
    List: List[TaskInfoOutput]
    Total: int
