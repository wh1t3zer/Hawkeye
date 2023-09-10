import websocket
import threading

def on_message(ws,message):
    print("接收消息:",message)

def on_error(ws,error):
    print("Error:",error)

def on_close(ws):
    print("连接关闭")

def on_open(ws):
    print("连接打开")
    #发送Websocket请求
    send_data(ws)
def send_data(ws):
    #构造WebSocket请求数据
    request_data ='dfdf'
    ws.send(request_data)

def run_websocket():
    #创建Websocket连接
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://124.222.224.186:8800/", on_message=on_message, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

run_websocket()
