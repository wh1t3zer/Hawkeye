from pydantic import BaseModel
from typing import List

class TrapPluginOutput(BaseModel):
    ID: int
    TrapID: str
    Name: str
    Author: str
    Protocol: str
    AppName: str
    HoneyPot: str
    Desc: str
    Content: str
    CreatedAt: str
    UpdatedAt: str
    IsDelete: int

    class Config:
        orm_mode = True

class TrapPluginListOutput(BaseModel):
    Total: int
    List: List[TrapPluginOutput]

class TrapPluginAddInput(BaseModel):
    TrapID: str
    Name: str
    Author: str
    Protocol: str
    AppName: str
    HoneyPot: str
    Desc: str
    Content: str

    class Config:
        orm_mode = True

class TrapPluginUpdateInput(BaseModel):
    ID: int
    TrapID: str
    Name: str
    Author: str
    Protocol: str
    AppName: str
    HoneyPot: str
    DescContent: str

    class Config:
        orm_mode = True
