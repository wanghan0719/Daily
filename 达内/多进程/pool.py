"""
进程池的使用
"""
from multiprocessing import Pool
from time import sleep, ctime
import os


# 进程池执行时间, 在进程池创建之前声明
def worker(msg):
    sleep(2)
    print(os.getpid(), '--', ctime(), ':', msg)


# 创建进程池
pool = Pool()
# 向进程池添加事件
for i in range(10):
    msg = "Tedu %d" % i
    pool.apply_async(worker, args=(msg,))

pool.close()  # 进程池关闭
pool.join()  # 进程池回收
