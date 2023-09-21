from pydantic import BaseModel

from micro.Nacos import register, getName


class User(BaseModel):
    ServerName: str
    RegistryAddress: str
    Services: list
    port: int


# 初始化
def InitUser(name, addr: str, port: int):
    return User(ServerName=name, RegistryAddress=addr, port=port)


# 连接注册中心
def RegistryConn(user: User):
    reg = register(user.ServerName, user.RegistryAddress, user.port)
    Services = getName(user.ServerName, user.RegistryAddress)
    user.Services = Services
    return user

# 获取节点
# def GetNodeByRamdom():
