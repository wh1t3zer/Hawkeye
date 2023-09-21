from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from utils.database import Base


class DomainInfo(Base):
    __tablename__ = "hawkeye_domain"
    ID = Column(Integer, primary_key=True, index=True, nullable=False)  # 自增主键
    AssetID = Column(Integer, nullable=False)  # 资产ID
    Domain = Column(String, nullable=False)  # 域名
    SubDomainList = Column(String, nullable=False)  # 子域列表
    Registrar = Column(String, nullable=False)  # 注册商
    RegisterDate = Column(String, nullable=False)  # 注册日期
    NameServer = Column(String, nullable=False)  # DNS解析地址
    DomainServer = Column(String, nullable=False)  # 域名解析器
    Status = Column(String, nullable=False)  # 状态


