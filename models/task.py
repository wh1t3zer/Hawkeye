import time

from sqlalchemy import Integer, Column, String

from utils.database import Base


class TaskInfo(Base):
    __tablename__ = "poc_task"
    ID = Column(Integer, primary_key=True, index=True, nullable=False)  # 自增主键
    RuleID = Column(Integer, nullable=False)  # web规则id
    Name = Column(String, nullable=False)  # 任务名
    TargetList = Column(String, nullable=False)  # 目标列表
    WebScan = Column(Integer, nullable=False)  # Web扫描
    PocScan = Column(Integer, nullable=False)  # Poc扫描
    AuthScan = Column(Integer, nullable=False)  # 权限扫描
    TrapScan = Column(Integer, nullable=False)  # 蜜罐识别
    Recursion = Column(Integer, nullable=False)  # 扫描周期
    Progress = Column(String, nullable=False)  # 扫描进程
    Percent = Column(Integer, nullable=False)  # 扫描百分比0-100
    Status = Column(String, nullable=False)  # 扫描状态
    CreateAt = time.time()  # 添加时间
    UpdateAt = time.time()  # 更新时间
    IsDelete = Column(Integer, nullable=False)  # 是否已删除；0：否；1：是
