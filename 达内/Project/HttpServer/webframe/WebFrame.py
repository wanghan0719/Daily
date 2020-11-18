"""
模拟网站的后端应用,提供网页或者其他数据
从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""
import json
import signal
from multiprocessing import Process
from socket import *
from urls import *
from settings import *


class Application:
    def __init__(self):
        self.address = (frame_ip, frame_port)
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sockfd.bind(self.address)
        signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    # 多进程并发服务
    def start(self):
        self.sockfd.listen(5)
        print("listen the port %d" % frame_port)
        while True:
            connfd, addr = self.sockfd.accept()
            p = Process(target=self.handle, args=(connfd,))
            p.setDaemon = True
            p.start()

    # 处理客户端请求的函数
    def handle(self, connfd):
        # 解析请求内容
        request = connfd.recv(1024).decode()
        # {'method':XX, 'info':XXX}
        request = json.loads(request)
        if request['method'] == 'GET':
            info = request['info']
            # 将请求内容分为两类 (网页,其他)
            if info == '/' or info[-5:] == '.html':
                response = self.get_html(info)
            else:
                response = self.get_data(info)
        elif request['method'] == 'POST':
            pass
        # response-->{'status':'200','data':'xxxx'}
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

    # 处理网页
    def get_html(self, info):
        if info == '/':
            filename = STATIC_DIR + "/index.html"
        else:
            filename = STATIC_DIR + info
        try:
            fd = open(filename)
        except Exception as e:
            # 网页不存在
            f = open(STATIC_DIR + "/404.html")
            return {'status': '404', 'data': f.read()}
        else:
            # 网页存在
            return {'status': '200', 'data': fd.read()}

    def get_data(self,info):
        for url,func in urls:
            if info == url:
                return {'status':'200','data':func()}
        return {'status': '404', 'data': 'Sorry'}



if __name__ == '__main__':
    app = Application()
    app.start()
