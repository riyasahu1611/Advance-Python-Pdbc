import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advpython')
cursor = connection.cursor()
sql = "update students set name = 'abhi' where id =2"
cursor.execute(sql)
connection.commit()
connection.close()
print("data Update Successfully")