"""
使用tcp完成，从客户端向服务端发送一个文件，
文件类型可能是二进制文件也可能是文本文件，文件自定

       温馨提示：
          发送端：  read() --> send()
          接受端：  recv() --> write()
"""

from socket import *

# 服务端接收文件

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

# 链接文件的发送端
c,addr = s.accept()
print("Connect from",addr)

# 接受文件名
filename = c.recv(1024).decode()

# 接收思路： 边接受内容，边写入文件
f = open(filename,'wb')
# 循环接收内容写入文件
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()





