"""
多个进程使用一个消息队列
"""
from multiprocessing import Queue, Process
from time import sleep

# 创建消息对列
q1 = Queue(3)
q2 = Queue(3)


def request():
    print("使用wx登录？")
    q1.put('请输入用户名密码')  # 写消息队列
    data = q2.get()
    print("获取信息:", data)


def get():
    data = q1.get()
    print("收到请求：", data)  # 读消息队列
    sleep(3)
    q2.put({'name': 'zhang', 'password': '123'})


p1 = Process(target=request)
p2 = Process(target=get)
p1.start()
p2.start()
p1.join()
p2.join()
