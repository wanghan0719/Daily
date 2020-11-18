"""
使用Process方法，创建两个子进程去同时复制一个文件的上
      半部分和下半部分，并分别写入到一个新的文件中。

       获取文件大小： os.path.getsize()
"""
from multiprocessing import Process
import os

file_name = 'yun.jpeg'
size = os.path.getsize(file_name)


# 复制上半部分
def top():
    # fr = open(file_name, 'rb')
    print(fr.fileno())
    fw = open('top.jpg', 'wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()


# 复制下半部分
def bot():
    # fr = open(file_name, 'rb')
    print(fr.fileno())
    fw = open('bot.jpg', 'wb')
    fr.seek(size // 2, 0)
    fw.write(fr.read())
    fr.close()
    fw.close()


fr = open(file_name, 'rb')
print(fr.fileno())
p1 = Process(target=top)
p2 = Process(target=bot)
p2.start()
p1.start()

p1.join()
p2.join()
