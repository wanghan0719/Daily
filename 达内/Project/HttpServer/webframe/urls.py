"""
可以处理的数据路由
声明了客户端发起那些申请时,我能够给你提供数据
"""
from views import *
# 路由列表
urls = [
    ('/time',show_time),
    ('/ai',ai),
    ('/bye',bye)
]