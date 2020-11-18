"""
客户端代码： 收集请求，发送请求，展示数据
"""

import getpass
import sys
from socket import *

ADDR = ('127.0.0.1', 8888)
s = socket()
s.connect(ADDR)


def do_register():
    while True:
        name = input("User:")
        passwd = getpass.getpass()
        passwd_ = getpass.getpass("Again:")

        # 基础的输入验证
        if passwd != passwd_:
            print("两次密码不一致")
            continue
        if (' ' in name) or (' ' in passwd):
            print("用户名或者密码不许有空格")
            continue

        # 用户名密码输入没有问题
        msg = "R %s %s" % (name, passwd)
        s.send(msg.encode())  # 发请求
        data = s.recv(128).decode()  # 等待结果
        if data == 'OK':
            print("注册成功")
        else:
            print("注册失败")
        return


def do_login():
    name = input("User:")
    passwd = getpass.getpass()
    msg = "L %s %s" % (name, passwd)
    s.send(msg.encode())  # 发送请求
    data = s.recv(128).decode()
    if data == 'OK':
        print("登录成功")
        login(name)  # 进入二级界面
    else:
        print("登录失败")


def do_hist(name):
    msg = "H %s" % name
    s.send(msg.encode())
    data = s.recv(1028).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print("您还没有历史记录哟")


# 二级界面函数
def login(name):
    while True:
        print("""
        =============Query===============
         1.查单词   2.历史记录    3.注销
        =================================
        """)
        cmd = input("输入选项:")
        if cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_hist(name)
        elif cmd == '3':
            return  # 从二级界面结束
        else:
            print("请输入正确选项")


# 　查询单词
def do_query(name):
    while True:
        word = input("单词:")
        if word == '##':
            break
        msg = "Q %s %s" % (name, word)
        s.send(msg.encode())
        # 　无论是找到单词还是其他都打印
        data = s.recv(2048).decode()
        print(data)


# 启动函数
def main():
    while True:
        print("""
        =============Welcome=============
         1.注册       2.登录        3.退出
        =================================
        """)
        cmd = input("输入选项:")
        if cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            s.send(b'E')
            sys.exit('谢谢使用')
        else:
            print("请输入正确选项")


if __name__ == '__main__':
    main()
