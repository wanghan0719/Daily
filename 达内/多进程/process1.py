"""
multiprocessing 模块创建进程
【1】 将需要子进程执行的事件封装为函数
【2】 通过模块的Process类创建进程对象,关联函数
【3】 可以通过进程对象设置进程信息及属性
【4】 通过进程对象调用start启动进程
【5】 通过进程对象调用join回收进程
"""
import multiprocessing as mp
from time import sleep

a = 1


# 进程函数
def fun():
    print("开始一个函数")
    sleep(2)
    global a
    print("a = ", a)
    a = 10000
    print("子进程结束")


# 创建进程对象
p = mp.Process(target=fun)
# 启动进程  执行fun
p.start()

# 父进程事件
sleep(3)
print('父进程干点事儿')
# 回收进程
p.join()
print("a:", a)
print("==============================")

"""15--19行
p = os.fork()
if pid == 0:
    fun()
    os._exit()
else:
    os.wait()
"""
