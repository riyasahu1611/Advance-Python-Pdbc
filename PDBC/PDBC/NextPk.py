import pymysql

pk = 0
connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advpython')
cursor = connection.cursor()
sql = "select max(id) from students"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))

for data in result:
    if data[0] is not None:
        pk = data[0]

connection.commit()
connection.close()

print(pk + 1)