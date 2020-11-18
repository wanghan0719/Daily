"""
lock 互锁放法演示
"""
from threading import Lock, Thread

a = b = 0
lock = Lock()  # 线程锁


def value():
    while True:
        lock.acquire()  # 上锁
        if a != b:
            print('a= %d,b=%d' % (a, b))
        lock.release()  # 解锁


t = Thread(target=value)
t.start()
while True:
    with lock:  # 上锁
        a += 1
        b += 1
                # 自动解锁

t.join()
