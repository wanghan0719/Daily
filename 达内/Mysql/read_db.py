"""
mysql.py
pymysql 操作的流程演示
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123',
                     database='stu',
                     charset='utf8')

# 生成游标对象(操作数据库,执行sql语句)
cur = db.cursor()

# name = input('查询的人名:')
# # 传入字符串时%s也要加上引号
# sql = "select * from class1 where name = '%s';" % name
# cur.execute(sql)  # 执行语句

# 查询性别为男,分数大于85
sql = "select * from class1 where sex = %s and score >%s;"
# 通过execute第二个参数列表传参给sql语句
cur.execute(sql,['m',85])


# # cur 可迭代对象，通过迭代获取select结果
# for i in cur:
#     print(i)

# 获取查询的第一个结果
# one_row = cur.fetchone()
# print(one_row)

# 获取多个查询结果
# many_row = cur.fetchmany(2)
# print(many_row)

# 获取所有结果
all_row = cur.fetchall()
print(all_row)

# 关闭游标及数据库连接
cur.close()
db.close()
