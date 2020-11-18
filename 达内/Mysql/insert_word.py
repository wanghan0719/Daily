import pymysql
import re

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123',
                     database='dict',
                     charset='utf8')
# 生成游标对象(操作数据库,执行sql语句)
cur = db.cursor()
# 插入单词
f = open('dict.txt', 'r')
arg_list = []
for line in f:
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]
    # print(tup)
    arg_list.append(tup)
f.close()
sql = "insert into words (word,mean) values (%s,%s);"
try:
    cur.executemany(sql, arg_list)
    db.commit()
except:
    db.rollback()
    # 关闭游标及数据库连接
    cur.close()
    db.close()
