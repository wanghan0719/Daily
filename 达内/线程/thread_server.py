"""
thread_server.py
重点代码

思路:
    创建监听套接字
    循环接收客户端连接请求
    当有新的客户端连接创建线程处理客户端请求
    主线程继续等待其他客户端连接
    当客户端退出，则对应分支线程退出
"""
from socket import *
from threading import Thread
import sys

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
# 创建TCP套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)
print("listen the port 8888")


# 客户端处理函数
def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')
    c.close()


while True:
    try:
        c, addr = s.accept()
        print("Connect with", addr)
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue
    # 创建线程
    t = Thread(target=handle, args=(c,))
    t.setDaemon(True) # 分支线程会随着主线程退出
    t.start()
