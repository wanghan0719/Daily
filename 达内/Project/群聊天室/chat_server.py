"""
chat room
env: python3.6
socket  udp  & fork
"""
from socket import *
import os
import sys

# 服务器地址
ADDR = ('127.0.0.1', 8888)

# 存储用户信息 {name:address}
user = {}


# 进入聊天室
def do_login(s, name, addr):
    if name in user or '管理' in name:
        s.sendto("该用户存在".encode(), addr)  # 返回登录成功消息
        return
    s.sendto(b'OK', addr)  # 返回登录成功消息

    # 告知其他人
    msg = "\n欢迎'%s'加入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name]: addr  # 加入字典


# 转发消息
def do_chat(s, name, text):
    msg = "\n%s:%s" % (name, text)
    for i in user:
        # 刨除其自己
        if i != name:
            s.sendto(msg.encode(), user[i])


# 处理退出
def do_quit(s, name):
    # 防止用户不再user
    if name not in user:
        return
    msg = "\n%s退出了聊天室" % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            # 他自己
            s.sendto(b'EXIT', user[i])
    del user[name]  # 删除用户


def request(s):
    """
    循环接收客户端请求，选择不同的功能函数处理
    """
    while True:
        data, addr = s.recvfrom(1024)  # 接收请求
        tmp = data.decode().split(" ", 2)  # 拆分请求
        # 根据不同的请求类型执行不同的函数(L,C,Q)
        if tmp[0] == 'L':
            do_login(s, tmp[1], addr)
        elif tmp[0] == 'C':
            do_chat(s, tmp[1], tmp[2])
        elif tmp[0] == 'Q':
            do_quit(s, tmp[1])


# 启动函数 启动服务
def main():
    # UDP 服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid == 0:
        while True:
            text = input("管理员消息：")
            msg = 'C 管理员 ' + text
            s.sendto(msg.encode(), ADDR)
    else:
        # 处理请求函数
        request(s)


if __name__ == '__main__':
    main()
