"""
同步互斥
"""
from threading import Thread, Event

s = None  # 全局变量，用于通讯
e = Event()


def yang():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()  # 解除wait阻塞


t = Thread(target=yang)
t.start()
print("说对指令就是自己人")
e.wait()  # 阻塞等待说口令
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他..")
t.join()
