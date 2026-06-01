import pymysql


def testinsert():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    sql = "INSERT INTO STUDENT VALUES (6, 'Anmol', 'Alampur')"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Inserted Successfully")


def testinsert1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    sql = "INSERT INTO STUDENT VALUES(9,'Anu','Sagar')"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Inserted1 Successfully")


def testinsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    sql = "INSERT INTO STUDENT VALUES(12, 'Mani', 'Bilaspur')"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Inserted2 Successfully")


def testInsert4(data={}):
    id = data['id']
    name = data['Name']
    Address = data['Address']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    sql = "insert into Student values(%s, %s, %s)"
    data = (id, name, Address)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('Data Inserted4 Successfully')

# testinsert()
# testinsert1()
# testinsert2()
testInsert4({'id': 15,'Name':'Aman','Address':'Agra'})
