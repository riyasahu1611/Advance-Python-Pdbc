import pymysql

pk = 0
connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
cursor = connection.cursor()
sql = "select * from students"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))

for data in result:
    print(data[0], data[1], data[2])


connection.commit()
connection.close()
