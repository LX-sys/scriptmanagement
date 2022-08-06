# -*- coding:utf-8 -*-
# @time:2022/7/2317:02
# @author:LX
# @file:oper_mysql.py
# @software:PyCharm


import pymysql


# 操作mysql数据库
class OperMysql:
    def __init__(self, host="43.138.57.51", port=3306, user="root", password="Lx984608061.", db="jsm"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    # 连接数据库
    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
            self.cursor = self.conn.cursor()
            print("连接数据库成功")
        except Exception as e:
            print(e)

    # 执行sql语句
    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    # 查询所有表
    def select_table(self):
        sql = "show tables"
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    # 查询数据库
    def select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 关闭数据库
    def close(self):
        self.cursor.close()
        self.conn.close()


class SMJPersonalInfo(OperMysql):
    table_name = "smj_personal_info"

    def __init__(self):
        super().__init__()
        self.connect()

    def get_personal_info(self,limit=100):
        sql = "select * from {} limit {};".format(SMJPersonalInfo.table_name,limit)
        return self.select(sql)

    # 删除数据(真实)
    def delete(self, username):
        self.cursor.execute('delete from {} where user="{}";'.format(SMJPersonalInfo.table_name,username))
        self.conn.commit()

    # 插入数据
    def insert(self, username, password,permission=0) -> int:
        if self.is_exist(username):
            print("用户名已存在")
            return 0

        self.cursor.execute('insert into {}(user,pwd,permission) values("{}","{}",{});'.format(SMJPersonalInfo.table_name,username, password,permission))
        self.conn.commit()
        return 200

    # 更新数据
    def update(self, username, password,permission) ->int:
        self.cursor.execute('update {} set pwd="{}",permission={} where user="{}";'.format(SMJPersonalInfo.table_name,password,permission,username))
        self.conn.commit()
        return 200

    # 判断用户名是否存在
    def is_exist(self, username)->bool:
        sql = "select * from {} where user='{}';".format(SMJPersonalInfo.table_name, username)
        if self.select(sql):
            return True
        return False

    # 登录验证
    def login(self, username, password)->bool:
        try:
            sql = "select * from {} where user='{}' and pwd='{}';".format(SMJPersonalInfo.table_name, username, password)
            if self.select(sql):
                return True
        except Exception as e:
            print(e)
        return False

    def close(self):
        self.cursor.close()
        self.conn.close()


class CardInfo(OperMysql):
    table_name = "card_info"

    def __init__(self):
        super(CardInfo, self).__init__()
        self.connect()

    def get_card_info(self,limit=100):
        sql = "select * from {} limit {}".format(CardInfo.table_name,limit)
        return self.select(sql)

    def get_name_card_info(self,user:str):
        sql = "select * from {} where user='{}';".format(CardInfo.table_name,user)
        # 预处理
        temp_card_info = self.select(sql)
        result = []
        for info in temp_card_info:
            # 构建信息
            card_info = {
                "id": info[0],
                "user": info[1],
                "ip": info[2],
                "number": info[3],
                "task": info[4],
                "count": info[5],
                "schedule": info[6],
                "scheduleAll": info[7].split("-"),
                "create_time":info[8],
                "update_time":info[9],
                "participator":info[10],
                "participatorAll":info[11].split("-"),
                "jspath":info[12],
            }
            result.append(card_info)
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()
if __name__ == '__main__':
    # 测试
    smj = CardInfo()
    print(smj.get_name_card_info('lx'))

