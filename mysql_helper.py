import pymysql

class MysqlHelper(object):
    def __init__(self):
        
        # 需要有连接
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='1234567890',
            database='mixed_fund',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        
        # 需要有游标
        self.cursor = self.conn.cursor()
    
    # 需要执行sql语句的函数  
    def execute_modify_sql(self, sql, data):
        self.cursor.execute(sql, data)
        self.conn.commit()
        
    def fetch_records(self, sql, filter_cond=None):
        
#         try:
        # 如果没有筛选条件
        if not filter_cond:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()

        else:
            self.cursor.execute(sql, filter_cond)
            results = self.cursor.fetchall()
        return results

#         finally:
#             self.cursor.close()
#             self.conn.close()
    
    # 需要有关闭游标和链接的删除函数
    def __del__(self):
        self.cursor.close()
        self.conn.close()