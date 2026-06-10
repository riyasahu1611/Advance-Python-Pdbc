import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='SCHOOL')
cursor = connection.cursor()
sql = "update marksheet set name = 'Ravi' where id =2"
i = cursor.execute(sql)
connection.commit()
connection.close()
print("Data Updated Successfully")