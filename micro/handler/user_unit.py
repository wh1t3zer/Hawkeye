class User:
    ServerName: str
    RegistryAddress: str
    Services: list


# 初始化
def InitUser(name, addr: str):
    return User(ServerName=name, RegistryAddress=addr)


# 连接注册中心
def RegistryConn():
