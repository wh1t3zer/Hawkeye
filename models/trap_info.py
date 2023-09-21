import time

from sqlalchemy import Column, Integer, String

from utils.database import Base


class TrapInfo(Base):
    __tablename__ = "hawkeye_trap"
    ID = Column(Integer, primary_key=True, index=True, nullable=False)  # 自增主键
    AssetID = Column(Integer, nullable=False)  # 资产id
    PortID = Column(Integer, nullable=False)  # 端口id
    PluginID = Column(Integer, nullable=False)  # 插件ID
    Verify = Column(String, nullable=False)  # 验证项
    TrapID = Column(String, nullable=False)  # 蜜罐ID
    Name = Column(String, nullable=False)  # 插件名
    Protocol = Column(String, nullable=False)  # 协议
    AppName = Column(String, nullable=False)  # 应用名
    HoneyPot = Column(String, nullable=False)  # 蜜罐名
    Desc = Column(String, nullable=False)  # 描述
    CreateAt = time.time()  # 添加时间
