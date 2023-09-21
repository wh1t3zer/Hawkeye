import random
import socket
import micro.Nacos


class GRPCServiceBase:
    def __init__(self, server_addr, server_port):
        # 初始化
        self.server_host = server_addr
        self.server_port = self._setattr(server_port)

    def _setattr(self, server_port):
        if not server_port:
            return self._generate_port()
        else:
            # 提供服务端口，检测是否被占用
            return self._generate_port(server_port)

    def _generate_port(self, port=None):
        # 生成随机端口
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            while True:
                if not port:
                    port = random.randrange(50000, 60000)
                result = sock.connect_ex(('127.0.0.1', port))
                if result != 0:
                    return port
                elif port:
                    # 当端口占用且为用户选择的情况
                    print("Failed bind port [::]:{}, Alerady in Running...".format(port))
                    return False
        except Exception as e:
            print("Failed generate server port,info:", e)
            return False

    def RegisterService(self, server_name, host, port, cluster_name):
        # 注册服务
        micro.Nacos.register(server_name=server_name, host=host, port=port, cluster_name=cluster_name)

    def GetService(self, server_name, host, port, cluster_name):
        service = micro.Nacos.getName(server_name=server_name, host=host, port=port, cluster_name=cluster_name)
        if not service:
            return None
        addr = "{}:{}".format(service['ip'], service['port'])
        return addr, service
