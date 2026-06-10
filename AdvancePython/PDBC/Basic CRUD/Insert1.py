import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='SCHOOL')
cursor = connection.cursor()
sql = "INSERT INTO MARKSHEET VALUES (6, 201,'Riya', 65, 45, 64)"
i = cursor.execute(sql)
connection.commit()
connection.close()
print("Data Inserted Successfully")