from sqlalchemy import Integer, Column, String

from utils.database import Base


class RuleInfo(Base):
    __tablename__ = "task_rule"
    ID = Column(Integer, primary_key=True, index=True, nullable=False)  # 自增主键
    AssetID = Column(Integer, nullable=False)  # 资产ID
    Port = Column(String, nullable=False)  # 端口
    Name = Column(String, nullable=False)  # 服务名
    State = Column(String, nullable=False)  # 状态
    Product = Column(String, nullable=False)  # 应用
    Version = Column(String, nullable=False)  # 版本
    Extrainfo = Column(String, nullable=False)  # 提取信息
    Conf = Column(String, nullable=False)  # 配置
    Cpe = Column(String, nullable=False)  # 指纹
