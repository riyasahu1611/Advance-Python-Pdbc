import pymysql
connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='rays')

try:
    connection.autocommit(False)
    cursor = connection.cursor()
    sql1 = "insert into marksheet values(19, 116, 'rahul', 13, 48, 38)"
    sql2 = "insert into marksheet values(20, 120, 'anmol', 13, 48, 38)"
    sql3 = "insert into marksheet values(19, 116, 'raj', 13, 48, 38)"

    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    connection.commit()
    print("Transaction committed successfully")
except Exception as e:
    connection.rollback()
    print("Transaction rolled back due to error:", e)