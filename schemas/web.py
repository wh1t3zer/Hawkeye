from pydantic import BaseModel
from typing import List


class WebInfoOutput(BaseModel):
    ID: int
    PortID: int
    StartURL: str
    Title: str
    Server: str
    ContentType: str
    LoginList: str
    UploadList: str
    SubDomain: str
    RouteList: str
    ResourceList: str

    class Config:
        orm_mode = True

class WebListOutput(BaseModel):
    Total: int
    List: List[WebInfoOutput]
