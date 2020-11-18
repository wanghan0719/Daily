"""
自定义进程类
"""
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, value):
        super().__init__()  # 加载父类__init__
        self.value = value

    def f1(self):
        print('步骤1')

    def f2(self):
        print('步骤2')

    def run(self):
        self.f1()
        self.f2()


p = MyProcess(3)
p.start()  # 自动运行 run()作为进程运行
p.join()
