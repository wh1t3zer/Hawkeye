from pydantic import BaseModel


class VulInfoOutput(BaseModel):
    ID: int
    AssetID: int
    Asset: str
    PortID: int
    PluginID: int
    AppName: str
    VulName: str
    VulType: str
    VerifyURL: str
    VerifyPayload: str
    VerifyResult: str
    ExploitURL: str
    ExploitPayload: str
    ExploitResult: str
    WebshellURL: str
    WebshellPayload: str
    WebshellResult: str
    TrojanURL: str
    TrojanPayload: str
    TrojanResult: str
    CreatedAt: str
    IsDelete: int
    SpareLine: int

    class Config:
        orm_mode = True


class VulListOutput:
    Total: int
    VulListOutput: VulInfoOutput
