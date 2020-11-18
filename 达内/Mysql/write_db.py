"""
write_db.py 写数据库
insert  update  delete
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
# 执行对数据库的写操作
try:
    # 执行增删改等语句
    # sql = "insert into class1 (name,age,score) values ('Dave',13,79);"
    # sql = "update class1 set sex = 'm' where name = 'Dave';"
    # sql = "delete from class1 where name = 'Dave';"

    # name = input("Name:")
    # age = input("Age:")
    # score = input("Score:")
    # 合成sql语句要顾虑整体的格式，保证sql正确
    # sql = "insert into class1 (name,age,score) \
    # values ('%s',%s,%s);"%(name,age,score)

    # 使用execute给sql传递参量
    # sql = "insert into class1 (name,age,score) \
    #     values (%s,%s,%s);"
    # cur.execute(sql,[name,age,score]) # 不要传递表名，字段名，关键字

    # cur.execute(sql)

    # 同时执行多次sql语句
    exe = []
    for i in range(3):
        name = input("Name:")
        age = input("Age:")
        score = input("Score:")
        exe.append((name, age, score))
    sql = "insert into cls1 (name,age,score) values (%s,%s,%s)"
    cur.executemany(sql, exe)

    db.commit()  # 将操作结果立即提交
except Exception as e:
    db.rollback()  # 事务回滚
    print(e)

# 关闭游标及数据库连接
cur.close()
db.close()
