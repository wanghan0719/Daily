"""
http server2.0
env: python 3.6
io多路复用和http训练
"""
from socket import *
from threading import Thread
from select import select


# 具体功能实现
class HTTPServer:
    def __init__(self, host='0.0.0.0', port=8000, dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host, port)
        # select 监控列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        # 实例化对象时直接创建套接字
        self.creat_socket()
        self.bind()

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("listen the port %d" % self.port)
        # 监控self.sockfd
        self.rlist.append(self.sockfd)
        # 循环监控IO发生
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    self.rlist.append(c)
                else:
                    # 浏览器发请求
                    self.handle(r)

    # 创建套接字
    def creat_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.sockfd.bind(self.address)

    def handle(self, connfd):
        # 获取http请求
        request = connfd.recv(1024 * 4).decode()
        # 客户端断开
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 简单的解析
        request_line = request.split('\n')[0]
        info = request_line.split(' ')[1]  # 提取请求内容
        print("请求内容:", info)
        # 将请求内容分为两类 (网页,其他)
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd, info)

    def get_html(self, connfd, info):
        if info == '/':
            filename = self.dir + "/index.html"
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except:
            # 网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += '\r\n'
            response += "Sorry...."
        else:
            # 网页存在
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += '\r\n'
            response += fd.read()
        finally:
            # 将结果发送给浏览器
            connfd.send(response.encode())

    # 处理其它
    @staticmethod
    def get_data(self, connfd, info):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html; charset=utf-8\r\n"
        response += '\r\n'
        response += "<h1>Waiting for httpserver 3.0</h1>"
        connfd.send(response.encode())


if __name__ == '__main__':
    """
    通过HTTPServer类可以快速的搭建一个服务,帮助我展示我的网页
    使用原则 : 1. 能够为使用者实现的尽量都实现
              2. 不能替用户决定的数据量让用户传入类中
              3. 不能替用户决定的功能让用户去重写
    """
    # 用户自己设定参数
    host = '0.0.0.0'
    port = 8000
    dir = "./static"  # 网页位置

    httpd = HTTPServer(host, port, dir)  # 实例化对象
    httpd.serve_forever()  # 启动服务
