import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
cursor = connection.cursor()
sql = "DELETE FROM Students WHERE ID =6"
cursor.execute(sql)
connection.commit()
connection.close()
print("Data Delete Successfully")