"""
进程对象属性
"""
from multiprocessing import Process
import time


def tm():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)


p = Process(target=tm,name='Jack',)
p.daemon = True
p.start()
print("Name:", p.name)  # 进程名称
print("PID", p.pid)  # 进程PID
print("is alive", p.is_alive())  # 是否在生命周期
p.join()