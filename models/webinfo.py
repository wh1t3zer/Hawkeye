from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from utils.database import Base


class WebInfo(Base):
    __tablename__ = "hawkeye_webinfo"
    ID = Column(Integer, primary_key=True, index=True, nullable=False)
    PortID = Column(Integer, index=True, nullable=False)    # 端口id
    StartURL = Column(String, nullable=False)       # 起始URL
    Title = Column(String, nullable=False)          # 站点标题
    Server = Column(String, nullable=False)         # Web服务器
    ContentType = Column(String, nullable=False)    # 内容类型
    LoginList = Column(String, nullable=False)      # 登录页列表
    UploadList = Column(String, nullable=False)     # 上传页面列表
    SubDomain = Column(String, nullable=False)      # 子域名列表
    RouteList = Column(String, nullable=False)      # URL列表
    ResourceList = Column(String, nullable=False)   # 资源列表
