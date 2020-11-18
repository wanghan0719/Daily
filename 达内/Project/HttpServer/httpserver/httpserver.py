"""
httpserver 主要功能 v3.0
获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
"""
import json
import re
import sys
from socket import *
from threading import Thread

from config import *


# 用于与webframe通信
def connect_frame(env):
    """
    将请求发送给WebFrame
    从WebFrame接收反馈数据
    """
    s = socket()
    try:
        s.connect((frame_ip, frame_port))
    except:
        print("连接不到WebFrame")
        return
    # 发送字典 {'method':xxx,'info':...}
    msg = json.dumps(env)
    s.send(msg.encode())   # 数据 --》 webframe
    # 从WebFrame 接收数据(json)
    data = s.recv(1024 * 1024 * 10).decode()
    return json.loads(data)


class HttpServer:
    def __init__(self):
        self.address = (HOST, PORT)
        self.create_socket()
        self.bind()


    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)
        self.host = self.address[0]
        self.port = self.address[1]

    def serve_forever(self):
        self.sockfd.listen(5)
        print("listen the port %d" % self.port)
        while True:
            connfd, addr = self.sockfd.accept()
            print("connect from",addr)
            client = Thread(target=self.handle, args=(connfd,))
            client.setDaemon(True)
            client.start()

    # 处理客户端请求的函数
    def handle(self, connfd):
        request = connfd.recv(4096).decode()
        pattern = r'(?P<method>[A-Z]+)\s+(?P<info>/\S*)'
        try:
            env = re.match(pattern, request).groupdict()
        except:
            connfd.close()
            return
        else:
            # {'status': '200', 'data': xxx}
            data = connect_frame(env)
            if data:
                self.response(connfd, data)

    # 组织响应并发送至客户端
    def response(self, connfd, data):
        # data-> {'status':'200','data':'xxxxxxx'}
        if data['status'] == '200':
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']
        elif data['status'] == '404':
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']
        response_data = responseHeaders + responseBody
        connfd.send(response_data.encode())


if __name__ == '__main__':
    httpd = HttpServer()
    httpd.serve_forever()  # 启动服务
