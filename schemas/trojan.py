from pydantic import BaseModel
from typing import List


class TrojanItemOutput(BaseModel):
    AssetID: int
    AssetIP: str
    PortID: int
    PortName: str
    RealServer: str
    CreateAT: str
    SpareLine: int

    class Config:
        orm_mode = True

class TrojanListOutput(BaseModel):
    Total: int
    List: List[TrojanItemOutput]

    class Config:
        orm_mode = True

class TrojanConnInput(BaseModel):
    AssetID: str
    AssetName: str
    SpareLine: int

    class Config:
        orm_mode = True