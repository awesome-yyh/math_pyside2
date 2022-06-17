import sys
import mysql.connector

class Mysql(object):

    def __init__(self):
        """初始化mysql连接"""
        try:
            self.conn = mysql.connector.connect(user='root', password='root', database='idmath113', use_unicode=True, auth_plugin='mysql_native_password')
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))
        self.cursor = self.conn.cursor()

    def query(self, table_id_m, questionId, red_word):
        """查询数据"""
        sql = 'select answer from ' + table_id_m + ' where questionID = %s and redWord = %s'
        self.cursor.execute(sql, (questionId, red_word,))
        return self.cursor.fetchall()

    def query_same(self, table_id_m, questionId):
        """查询数据"""
        sql = 'select redWord, answer from ' + table_id_m + ' where questionID = %s'
        self.cursor.execute(sql, (questionId,))
        return self.cursor.fetchall()

    def insert(self,table_id, val):
        """ 插入一行记录"""
        sql = 'insert ignore into ' + table_id + ' (questionID, redWord, answer) values (%s, %s, %s)'       
        try:
            self.cursor.execute(sql, val)
            self.conn.commit()
        except:
            self.conn.rollback()

    def dele(self,table_id, questionId, red_word):
        """ 删除一行记录"""
        sql = 'DELETE FROM ' + table_id + ' WHERE questionID = %s AND redWord=%s '
        try:
            self.cursor.execute(sql, (questionId, red_word,))
            self.conn.commit()
        except:
            self.conn.rollback()

    def __del__(self):
        """ 关闭mysql连接 """
        if self.conn:
            self.conn.close()

if __name__ == '__main__':
    # 创建一个mysql类
    mysql = Mysql()
    table_id = 'm75'

    value = mysql.query_same(table_id, '1817067')
    if value:
        values = '$'.join([n for t in value for n in t])
        values = values.split('$')
        print(values[0])
        # print(value[0])
        # print(value[1])
    else:
        print('不存在')

    # inputt = '4*x+y^2=9, x=2*y'
    # values = mysql.query(table_id, inputt)
    # if values:
        values = ' '.join([n for t in values for n in t])
        print(values)

    # premeter = 'y=a*x-x^2, y=b*x,6,2'
    # answer = '32/ 3 '
    # val = [premeter, answer]
    # mysql.insert(table_id, val)
    # print('插入成功')
