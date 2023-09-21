from pydantic import BaseModel
from typing import List


class PocPluginAddInput(BaseModel):
    VulID: str
    VulName: str
    VulType: str
    VulDate: str
    Version: str
    Author: str
    AppPowerLink: str
    AppName: str
    AppVersion: str
    Desc: str
    Cnnvd: str
    CveID: str
    Rank: int
    DefaultPorts: str
    DefaultService: str
    Content: str

    class Config:
        orm_mode = True


class PocPluginInfoOutput(BaseModel):
    ID: int
    VulID: str
    VulName: str
    VulType: str
    VulDate: str
    Version: str
    Author: str
    AppPowerLink: str
    AppName: str
    AppVersion: str
    Desc: str
    Cnnvd: str
    CveID: str
    Rank: int
    DefaultPorts: str
    DefaultService: str
    Content: str
    UpdatedAt: str
    CreatedAt: str
    IsDelete: int

    class Config:
        orm_mode = True


class PocPluginListOutput(BaseModel):
    Total: int
    List: List[PocPluginInfoOutput]
