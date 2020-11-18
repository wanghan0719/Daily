# 发送文件
from socket import *
from time import sleep

s = socket()
s.connect(('127.0.0.1',8888))

# 思路 ： 边读取边发送
filename = input("File:")
file = filename.split('/')[-1]
s.send(file.encode()) # 先发送文件名称

# 发送延迟，给接收端充分的时间把文件名字先接收
sleep(0.5)

f = open(filename,'rb')

while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)

f.close()
s.close()