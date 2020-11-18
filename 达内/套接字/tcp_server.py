"""
tcp_server.py
重点代码

测试使用命令 ： telnet 127.0.0.1 8888
"""
import socket

# 创建TCP套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 设置端口立即可以被重用,须在bind之前完成
sockfd.setsockopt(socket.SOL_SOCKET,
                  socket.SO_REUSEADDR, 1)

# 绑定地址
sockfd.bind(('0.0.0.0', 8888))

# 设置监听
sockfd.listen(3)

# 等待客户端链接
while True:
    print("等待链接....")
    try:
        connfd, addr = sockfd.accept()
        print("链接了：", addr)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
        continue
    # 收发消息
    while True:
        data = connfd.recv(1024)
        # 客户端退出服务端立即得到空字串
        if not data:
            break
        # 客户端退出
        # if data == b'##':
        #     break
        print("收到：", data.decode())
        n = connfd.send('收到'.encode())  # bytes
        print("发送了 %d bytes" % n)
    connfd.close()

# 关闭套接字
sockfd.close()
