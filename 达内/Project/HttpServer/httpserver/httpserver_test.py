"""
测试httpserver的功能
"""
import json
from socket import *

s = socket()
s.bind(('0.0.0.0', 8080))
s.listen(3)
while True:
    c, addr = s.accept()
    data = c.recv(1024).decode()
    print(json.loads(data))
    d = {'status': 200, 'data': 'OK'}
    msg = json.dumps(d)
    c.send(msg.encode())
