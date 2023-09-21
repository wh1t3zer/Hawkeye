import time

from sqlalchemy import Column, Integer, String

from utils.database import Base


class PocPlugin(Base):
    __tablename__ = "poc_plugin"
    ID = Column(Integer, primary_key=True, index=True, nullable=False)  # 自增主键
    vulID = Column(String, nullable=False)  # vul_id
    VulName = Column(String, nullable=False)  # 漏洞名
    VulType = Column(String, nullable=False)  # 漏洞类型
    VulDate = time.time()  # 漏洞发布日期
    Version = Column(String, nullable=False)  # 插件版本
    Author = Column(String, nullable=False)  # 编写者
    AppPowerLink = Column(String, nullable=False)  # 产商链接
    AppName = Column(String, nullable=False)  # 应用名
    AppVersion = Column(String, nullable=False)  # 应用版本
    Desc = Column(String, nullable=False)  # 漏洞描述
    Cnnvd = Column(String, nullable=False)  # cnnvd
    CveID = Column(String, nullable=False)  # cve_id
    Rank = Column(Integer, nullable=False)  # 危险等级
    DefaultPorts = Column(String, nullable=False)  # 默认端口
    DefaultService = Column(String, nullable=False)  # 默认服务
    Content = Column(String, nullable=False)  # 脚本内容
    UpdateAt = time.time()  # 更新时间
    Create = time.time()  # 创建时间
    IsDelete = Column(Integer, nullable=False)  # 是否删除
