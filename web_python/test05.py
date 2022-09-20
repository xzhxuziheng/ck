"""
coder: xuziheng
date: 2022/8/31 15:28
"""
# 连接MySQL上下文管理器
import pymysql


class DB:
    def __init__(self, data_conf):
        self.con = pymysql.connect(**data_conf)
        self.cursor = self.con.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.con.close()


DATABASES_CONF = dict(
    host='',
    user='',
    password='',
    database='',
    port='',
    charset='ustf8'
)

with DB(DATABASES_CONF) as cur:
    cur.execute('select * from user')
    print(cur.fetchone())
