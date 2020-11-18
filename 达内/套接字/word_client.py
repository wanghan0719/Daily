from socket import *

# 服务端地址
ADDR = ('127.0.0.1',8888)

sockfd = socket(AF_INET,SOCK_DGRAM)

# 循环收发消息
while True:
    data = input("Word>>")
    if not data:
        break
    # 发送单词
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(2048)
    print(msg.decode())

sockfd.close()

