from sqlalchemy import Column, Integer, String

from utils.database import Base


class AuthInfo(Base):
    ID = Column(Integer, primary_key=True, index=True, nullable=False)  # 自增主键
    AssetID = Column(Integer, nullable=False)  # 资产id
    PortID = Column(Integer, nullable=False)  # 端口id
    Target = Column(String, nullable=False)  # 目标
    Service = Column(String, nullable=False)  # 服务
    Username = Column(String, nullable=False)  # 用户名
    Password = Column(String, nullable=False)  # 密码
    Command = Column(String, nullable=False)  # 验证命令
