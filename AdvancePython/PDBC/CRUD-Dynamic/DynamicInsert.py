import pymysql


def testInsert1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "insert into marksheet values(7, 202, 'abc', 34, 48, 38)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='school')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (8, 203, 'xyz', 78, 67, 56)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert3(id, rollNo, name, physics, chemistry, maths):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (id, rollNo, name, physics, chemistry, maths)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert4(data={}):
    id = data['id']
    rollNo = data['rollNo']
    name = data['name']
    physics = data['physics']
    chemistry = data['chemistry']
    maths = data['maths']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (id, rollNo, name, physics, chemistry, maths)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


# testInsert1()
# testInsert2()
# testInsert3(9, 204, 'pqr', 89, 77, 67)

params = {}
params['id'] = 11
params['rollNo'] = 404
params['name'] = 'klj'
params['physics'] = 95
params['chemistry'] = 98
params['maths'] = 65

print(params)
testInsert4(params)
