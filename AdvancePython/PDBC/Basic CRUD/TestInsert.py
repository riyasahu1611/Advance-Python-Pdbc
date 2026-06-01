import pymysql
connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advpython')
cursor = connection.cursor() # execute
sql = "INSERT INTO students VALUES (5, 'Riya', 'Dewas')"
i = cursor.execute(sql)
connection.commit()
connection.close()
print("Data Added Successfully",i)