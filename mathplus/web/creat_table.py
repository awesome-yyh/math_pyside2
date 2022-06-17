# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='root', database='idmath113', use_unicode=True, auth_plugin='mysql_native_password')
cursor = conn.cursor()
# cursor.execute("CREATE DATABASE idmath113") #创建数据库
# database='idmath113'
# 创建user表:
# cursor.execute('create table mp112 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table mp113 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m201 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m202 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m203 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m204 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m205 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m206 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m207 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m208 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')

# cursor.execute('create table m301 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m302 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m303 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m304 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m305 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m306 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m307 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m308 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m309 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m310 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m311 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')

# cursor.execute('create table m401 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m402 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m403 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m404 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m405 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m406 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m407 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m408 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute('create table m409 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')

cursor.execute('create table p112 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
cursor.execute('create table p113 (questionID varchar(10) , redWord varchar(1000), answer varchar(10000))')
# cursor.execute("DELETE FROM m64 WHERE questionID = '3693039' AND redWord='60,0.7,130' ")

# 提交事务:
conn.commit()
cursor.close()

cursor.close()
conn.close()