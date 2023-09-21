import time

from sqlalchemy import Column, Integer, String

from utils.database import Base


class PocTask(Base):
    __tablename__ = "poc_task"
    ID = Column(Integer, primary_key=True, index=True, nullable=False)  # 自增主键
    AssetID = Column(Integer, nullable=False)  # 资产ID
    PortinfoID = Column(Integer, nullable=False)  # 端口ID
    Status = Column(String, nullable=False)  # 任务状态
    TargetList = Column(Integer, nullable=False)  # 目标列表
    TaskName = Column(Integer, nullable=False)  # 任务名
    Recursion = Column(Integer, nullable=False)  # 扫描周期
    PluginList = Column(Integer, nullable=False)  # 插件列表
    UpdateAt = time.time()  # 更新时间
    CreateAt = time.time()  # 创建时间
    IsDelete = Column(Integer, nullable=False)  # 是否删除
