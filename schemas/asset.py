from pydantic import BaseModel


class AssetListOutput(BaseModel):
    total: int

    class Config:
        orm_mode = True


class AssetInfoOutput(BaseModel):
    id: int
    task_id: int
    task_name: str
    task_status: str
    ip: str
    gps: str
    area: str
    isp: str
    os: str
    vendor: str
    create_at: str
    port_array: list
    vul_count: int

    class Config:
        orm_mode = True
