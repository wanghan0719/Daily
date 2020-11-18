"""
数据处理模块
"""
import hashlib

import pymysql


# 　密码转换函数
def change_passwd(passwd):
    salt = '*#06#'
    hash = hashlib.md5(salt.encode())  # 生成加密对象
    hash.update(passwd.encode())  # 算法加密处理
    passwd = hash.hexdigest()  # 获取加密后的字串
    return passwd


class Database:
    def __init__(self, host='localhost', port=3306, user=None, password=None, database=None, charset='utf8'):
        self.db = pymysql.connect(host=host,
                                  port=port,
                                  user=user,
                                  password=password,
                                  database=database,
                                  charset=charset)
        self.cur = None

    def create_cur(self):
        self.cur = self.db.cursor()

    def close(self):
        if self.cur:
            self.cur.close()
        self.db.close()

    def register(self, name, passwd):
        # 判断该用户名是否存在
        sql = "select name from dict.user where name='%s';" % name
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return False
        # 插入用户
        passwd = change_passwd(passwd)
        try:
            sql = "insert into dict.user (name,password) values (%s,%s)"
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def login(self, name, passwd):
        passwd = change_passwd(passwd)  # 转换密码

        # 和数据库信息进行比对
        sql = "select name,password from dict.user where name=%s and password=%s;"
        self.cur.execute(sql, [name, passwd])
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    # 查单词
    def query(self, word):
        sql = "select mean from dict.words where word=%s;"
        self.cur.execute(sql, [word])
        r = self.cur.fetchone()
        if r:
            return r[0]

    def insert_history(self, name, word):
        sql = "insert into dict.hist1 (name,word) values (%s,%s);"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except:
            self.db.rollback()

    def history(self, name):
        sql = "select name,word,time from dict.hist1 where name=%s order by time limit 10"
        self.cur.execute(sql, name)
        return self.cur.fetchall()