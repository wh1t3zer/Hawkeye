import time
import nacos
from utils.file import read_config

config = read_config('micro.yaml')
port = read_config('base.yaml')['http']['port']

# Nacos服务器地址
HOST = str(config['nacos']['cluster-addr']).split(',')
# 命名空间
NAMESPACE = config['nacos']['namespace']
# 服务名
SERVERNAME = config['nacos']['servername']
# 账号信息
USERNAME = config['nacos']['username']
PASSWORD = config['nacos']['password']


def register():
    # 获取Nacos客户端工具，四个参数(Nacos服务器地址，命名空间，用户名，密码)
    for SERVER_ADDRESSES in HOST:
        client = nacos.NacosClient(
            server_addresses=SERVER_ADDRESSES, namespace=NAMESPACE, username=USERNAME, password=PASSWORD
        )
        client.add_naming_instance(SERVERNAME, "localhost", port)
        # print(client.get_config('test','DEFAULT_GROUP'))


def beat():
    while True:
        for SERVER_ADDRESSES in HOST:
            client = nacos.NacosClient(
                server_addresses=SERVER_ADDRESSES, namespace=NAMESPACE, username=USERNAME,password=PASSWORD
            )
            client.add_naming_instance(SERVERNAME, "localhost", port)
            # print('心跳一次')
        time.sleep(5)


def init_nacos():
    print("service for nacos")
    register()
    beat()
