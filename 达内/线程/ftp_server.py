"""
ftp 服务器  服务端
env: python3.6
多线程并发, socket, 文件IO
"""
from socket import *
from threading import Thread
import sys
import os
from time import sleep

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
ftp = "/home/wang/FTP/"  # 文件库位置


class PTPServer(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == 'Q':
                return
            elif data == 'L':
                self.do_list()
            elif data[0] == 'D':
                filename = data.split(" ")[-1]
                self.do_get(filename)
            elif data[0] == 'U':
                filename = data.split(" ")[-1]
                self.do_put(filename)

    # 发送文件列表
    def do_list(self):
        files = os.listdir(ftp)
        if not files:
            self.connfd.send('文件列表为空'.encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)

        # for file in files:
        #     self.connfd.send(file.encode())
        # self.connfd.send(b'##')

        # 发送文件列表
        filelist = '\n'.join(files)
        self.connfd.send(filelist.encode())

    def do_get(self, filename):
        try:
            f = open(ftp + filename, 'rb')
        except Exception:
            # 打开失败
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    # 上传文件
    def do_put(self, filename):
        if os.path.exists(ftp + filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b'OK')
        # 接收文件
        f = open(ftp + filename, 'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()


def main():
    # 创建TCP套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    print("listen the port 8888")
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
        t = PTPServer(c)
        t.setDaemon(True)  # 分支线程会随着主线程退出
        t.start()


if __name__ == '__main__':
    main()
