import pymysql
# import cx_Oracle -- 오라클 연동
# self.db = cx_Oracle.connect(<<USER_NAME>>/<<PWD>>@<<HOST>>:<<PORT>>/<<SERVICE_NAME>>)

class DbConfig:
    db_config = {}
    db = None
    cursor = None

    def __init__(self, db_info=None):
        if str(type(db_info)) == "<class 'str'>":
            sysNm = str(db_info)
            if sysNm == 'zero':
                self.db_config = {
                    'host': 'zero.cqjpoyzx2xld.ap-northeast-2.rds.amazonaws.com' 
                    , 'user': 'zero'
                    , 'password': 'tkrkwl1564!'
                    , 'db': 'zero'
                }
            else:  # 로컬에서 테스트 진행 시
                self.db_config = {
                    'host': "zero.cqjpoyzx2xld.ap-northeast-2.rds.amazonaws.com"
                    , 'user': 'zero'
                    , 'password': 'tkrkwl1564!'
                    , 'db': 'innodb'
                }
        elif str(type(db_info)) == "<class 'dict'>":
            print(type(db_info))

    def opendb(self):
        self.db = pymysql.connect(**self.db_config)
        self.db.set_charset('utf8mb4')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def closedb(self):
        self.db.close()

    def select(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def update(self, sql):
        return self.cursor.execute(sql)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()