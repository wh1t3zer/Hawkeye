import time
import nacos
from nacos import NacosClient
from utils.file import read_config

config = read_config('micro.yaml')
HTTP_PORT = read_config('base.yaml')['http']['port']

# Nacos服务器地址
IP = str(config['nacos']['cluster-addr']).split(',')
# 命名空间
NAMESPACE = config['nacos']['namespace']
# 服务名
SERVERNAME = config['nacos']['servername']
# 账号信息
USERNAME = config['nacos']['username']
PASSWORD = config['nacos']['password']
PORT = config['nacos']['port']

'''
server_name 注册的服务名
host 注册服务的地址
port 注册服务的端口
注册服务
'''


def register(server_name, host, port, cluster_name):
    # 获取Nacos客户端工具，四个参数(Nacos服务器地址，命名空间，用户名，密码)
    for SERVER_IP in IP:
        SERVER_ADDR = "{}:{}".format(SERVER_IP, PORT)
        client = nacos.NacosClient(
            server_addresses=SERVER_ADDR, namespace=NAMESPACE, username=USERNAME, password=PASSWORD
        )
        # client.add_naming_instance(service_name=server_name, ip=host, port=port)
        return client.add_naming_instance(service_name=server_name, ip=host, port=port, cluster_name=cluster_name)


'''
server_name 注册的服务名
host 注册的服务地址
port 注册服务的端口
'''


def getName(server_name, host, port, cluster_name):
# def getName(server_name):
    # 获取Nacos客户端工具，四个参数(Nacos服务器地址，命名空间，用户名，密码)
    for SERVER_IP in IP:
        SERVER_ADDR = "{}:{}".format(SERVER_IP, PORT)
        client = nacos.NacosClient(
            server_addresses=SERVER_ADDR, namespace=NAMESPACE, username=USERNAME, password=PASSWORD
        )
        # client.get_naming_instance(server_name, host, port, cluster_name)
        return client.get_naming_instance(service_name=server_name, ip=host, port=port, cluster_name=cluster_name)


'''
server_name 注册的服务名
host 注册服务的地址
port 注册服务的端口
保持心跳
'''


def beat(server_name, server_host, server_port, cluster_name):
    # 获取Nacos客户端工具，四个参数(Nacos服务器地址，命名空间，用户名，密码)
    for SERVER_IP in IP:
        SERVER_ADDR = "{}:{}".format(SERVER_IP, PORT)
        client = nacos.NacosClient(
            server_addresses=SERVER_ADDR, namespace=NAMESPACE, username=USERNAME, password=PASSWORD
        )
        while True:
            client.send_heartbeat(server_name, server_host, server_port, cluster_name=cluster_name)
            # print('心跳一次')
            time.sleep(5)


def init_nacos():
    # 主服务保持连接
    register(SERVERNAME, "127.0.0.1", HTTP_PORT, 'None')
    service = getName(SERVERNAME,"127.0.0.1", HTTP_PORT, 'None')
    beat(service['service'], service['ip'], service['port'], service['clusterName'])


if __name__ == '__main__':
    init_nacos()
