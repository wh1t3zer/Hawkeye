import time

from sqlalchemy import Integer, Column, String

from utils.database import Base


class TrapPluginInfo(Base):
    __tablename__ = "trap_plugin"
    ID = Column(Integer, primary_key=True, index=True, nullable=False)  # 自增主键
    TrapID = Column(String, nullable=False)  # 蜜罐ID
    Name = Column(String, nullable=False)  # 插件名
    Author = Column(String, nullable=False)  # 编写者
    Protocol = Column(String, nullable=False)  # 协议
    AppName = Column(String, nullable=False)  # 应用名
    HoneyPot = Column(String, nullable=False)  # 蜜罐名
    Desc = Column(String, nullable=False)  # 描述
    Content = Column(String, nullable=False)  # 脚本内容
    CreateAt = time.time()  # 添加时间
    UpdateAt = time.time()  # 更新时间
    IsDelete = Column(Integer, nullable=False)  # 是否已删除；0：否；1：是
