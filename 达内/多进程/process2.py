"""
Process 同时创建多个子进程
"""
from multiprocessing import Process
from time import sleep
import os


def th1():
    sleep(3)
    print('吃饭')
    print(os.getppid(), '---', os.getpid())


def th2():
    sleep(2)
    print('睡觉')
    print(os.getppid(), '---', os.getpid())


def th3():
    sleep(4)
    print('打豆豆')
    print(os.getppid(), '---', os.getpid())


things = [th1, th2, th3]
job = []
for th in things:
    p = Process(target=th)
    job.append(p)  # 使用列表将进程对象存储
    p.start()
for ｉ in job:
    p.join()
