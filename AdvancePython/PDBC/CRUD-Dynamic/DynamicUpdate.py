import pymysql


def testUpdate1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    sql = "update student set name = 'Ayush' where id =2"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    sql = "update student set name = %s where id = %s"
    data = ('Rohit', 1)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated2 successfully')


def testUpdate3(id, name):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    sql = "update student set name = %s where id = %s"
    data = (id, name)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated3 successfully')


def testInsert4(data):
    id = data['id']
    name = data['Name']
    address = data['address']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    sql = "update student set id= %s, name= %s, address= %s where id = %s"
    data = (id, name, address, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted4 successfully')


testUpdate1()
# testUpdate2()
# testUpdate3('Aman', 3)

#
# params = {}
# params['id'] = 2
# params['Name'] = 'Amolika'
# params['address'] = 'Delhi'

# testInsert4(params)