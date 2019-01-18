# Created by Helic on 2017/10/29
import pymysql

# # 打开数据库连接
# db = pymysql.connect("localhost", "helic", "root1234", "ruisi")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()

# 打开数据库连接
db = pymysql.connect(host="localhost", port=3306, user="helic", passwd="root1234", db="ruisi", charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

record_row = ['思思', '3岁', '徐', '爸爸', '18810559266', '北京市海淀区', '保福寺', '周六', 'jn']

# SQL 查询语句
sql = 'INSERT into record(`child_name`, `child_age`, `client_name`, `client_gender`, `phone_number`,`client_location`,`reserve_location`,`reserve_time`,`dialog_content`) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (record_row[0], record_row[1], record_row[2], record_row[3], record_row[4], record_row[5], record_row[6],record_row[7], record_row[8])

try:
    # 执行SQL语句
    cursor.execute(sql)
except Exception:
    print("Error: unable to fetch data")
cursor.close()

# 关闭数据库连接
db.commit()
db.close()

