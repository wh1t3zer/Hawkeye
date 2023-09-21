import time

from sqlalchemy import Column, Integer, String

from utils.database import Base


class VulInfo(Base):
    __tablename__ = "hawkeye_vulinfo"
    ID = Column(Integer, primary_key=True, index=True, nullable=False)  # 自增主键
    AssetID = Column(Integer, nullable=False)  # 资产id
    PortID = Column(Integer, nullable=False)  # 端口id
    PluginID = Column(Integer, nullable=False)  # 插件ID
    VerifyURL = Column(String, nullable=False)  # 漏洞验证URL
    VerifyPayload = Column(String, nullable=False)  # 漏洞验证Payload
    VerifyResult = Column(String, nullable=False)  # 漏洞验证Result
    ExploitURL = Column(String, nullable=False)  # 漏洞利用URL
    ExploitPayload = Column(String, nullable=False)  # 漏洞利用Payload
    ExploitResult = Column(String, nullable=False)  # 漏洞利用Result
    WebshellURL = Column(String, nullable=False)  # Webshell URL
    WebshellPayload = Column(String, nullable=False)  # Webshell Payload
    WebshellResult = Column(String, nullable=False)  # Webshell Result
    TrojanURL = Column(String, nullable=False)  # Trojan URL
    TrojanPayload = Column(String, nullable=False)  # Trojan Payload
    TrojanResult = Column(String, nullable=False)  # Trojan Result
    CreateAt = time.time()  # 添加时间
    IsDelete = Column(Integer, nullable=False)  # 是否已删除；0：否；1：是
