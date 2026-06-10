import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='SCHOOL')
cursor = connection.cursor()
sql = "DELETE FROM MARKSHEET WHERE ID =4"
i = cursor.execute(sql)
connection.commit()
connection.close()
print("Data Deleted Successfully")