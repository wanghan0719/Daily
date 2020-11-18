"""
逻辑处理模块
"""

import signal
import sys
from multiprocessing import Process
from socket import *
from time import sleep

from dict_db import *

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

# 链接数据库
db = Database(user='root', password='123', database='dict')


# 处理注册
def do_register(c, name, passwd):
    if db.register(name, passwd):
        c.send(b'OK')  # 告诉客户端一下结果
    else:
        c.send(b'Fail')


# 　处理登录
def do_login(c, name, passwd):
    if db.login(name, passwd):
        c.send(b'OK')  # 告诉客户端一下结果
    else:
        c.send(b'Fail')


# 单词查询
def do_query(c, name, word):
    db.insert_history(name, word)  # 插入历史记录
    mean = db.query(word)
    if not mean:
        c.send('没有找到该单词'.encode())
    else:
        msg = "%s : %s" % (word, mean)
        c.send(msg.encode())


# 历史记录
def do_hist(c, name):
    data = db.history(name)
    if not data:
        c.send(b'Fail')
        return
    else:
        c.send(b'OK')
    # data->((name,word,time),(),())
    for i in data:
        msg = "%s  %-16s  %s" % i
        c.send(msg.encode())
    sleep(1)
    c.send(b'##')


# 具体处理客户端请求


def handle(c):
    db.create_cur()  # 每个子进程单独生成自己的游标对象
    # 循环接收来自客户端的请求，然后调用相应的函数进行处理
    while True:
        data = c.recv(1024).decode()
        # print(c.getpeername(),':',data)
        tmp = data.split(' ')  # 解析请求
        if not data or tmp[0] == 'E':
            return
        elif tmp[0] == 'R':
            # R name passwd
            do_register(c, tmp[1], tmp[2])
        elif tmp[0] == 'L':
            # L name passwd
            do_login(c, tmp[1], tmp[2])
        elif tmp[0] == 'Q':
            # Q name word
            do_query(c, tmp[1], tmp[2])
        elif tmp[0] == 'H':
            do_hist(c, tmp[1])


# 启动函数
def main():
    # 创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # 循环等待客户端链接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            db.close()  # 关闭了数据库
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        #  有客户链接
        p = Process(target=handle, args=(c,))
        p.daemon = True
        p.start()


if __name__ == '__main__':
    main()
