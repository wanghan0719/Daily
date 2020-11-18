"""
fork 函数创建新进程
获取进程PID
"""
import os
print('============')
a=1
pid = os.fork()
if pid <0:
    print('Error')
elif pid ==0:
    print('Child PID=',os.getpid())  # 从子进程中获取自己的PID
    print('Parent PID=',os.getppid())  # 从子进程中获取父进程的PID
    print('Child Process')
    print('a=',a)
    a =10000
else:
    os.getpid()
    print('get child Pid',pid)  # 父进程中获取子进程的PID
    print('Parent process')
    print('a=', a)

