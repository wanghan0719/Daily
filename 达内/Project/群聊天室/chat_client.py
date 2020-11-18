"""
chat room
* 发送请求，获取结果
"""
from socket import *
import os
import sys

# 服务器地址
ADDR = ('127.0.0.1', 8888)


def send_msg(s, name):
    while True:
        try:
            text = input('发言：')
        except KeyboardInterrupt:
            text = 'quit'
        if text.strip() == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" % (name, text)
        s.sendto(msg.encode(), ADDR)


def recv_msg(s):
    while True:
        try:
            data, addr = s.recvfrom(1024 * 1024)
        except KeyboardInterrupt:
            sys.exit()
        # 从服务器收到退出指令
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode() + '\n发言', end='')


def login(s):
    while True:
        name = input("请输入用户名：")
        msg = 'L ' + name
        # 发送登录请求
        s.sendto(msg.encode(), ADDR)
        # 接收登录请求结果
        data, addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print("进入聊天室成功")
            return name
        else:
            print(data.decode())


# 启动函数
def main():
    # UDP 服务端
    s = socket(AF_INET, SOCK_DGRAM)
    # 进入聊天室
    name = login(s)  # 登录
    pid = os.fork()
    if pid < 0:
        sys.exit('Error')
    elif pid == 0:
        send_msg(s, name)  # 子进程发消息
    else:
        recv_msg(s)  # 父进程收消息


if __name__ == '__main__':
    main()
