import pymysql

connection= pymysql.connect(host='localhost', port=3306, user='root', password='root', database='rays')
connection.autocommit(True)
cursor = connection.cursor()
sql1 = "insert into marksheet values(16, 116, 'raj', 13, 48, 38)"
sql2 = "insert into marksheet values(17, 117, 'raj', 13, 48, 38)"
sql3 = "insert into marksheet values(16, 116, 'raj', 13, 48, 38)"

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
connection.close()
print("data get successfully")