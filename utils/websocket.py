# import socket
#
#
# # 建立socket链接
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 防止linux/mac报错
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# # 服务器IP
# sock.bind(('127.0.0.1', 8000))
# conn, address = sock.accept()
# data = conn.recv(1024)  # 获取客户端发送的消息

from fastapi import WebSocket, FastAPI
from starlette.testclient import TestClient

app = FastAPI()

@app.websocket("/ws")
def web(websocket: WebSocket):
    print()


