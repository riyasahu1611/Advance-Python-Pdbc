import pymysql


def testUpdate1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "update marksheet set rollNo = 104, name = 'ritu', phy = 99, chm = 99, maths = 99 where id = 2"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "update marksheet set rollNo = %s, name = %s, phy = %s, chM = %s, maths = %s where id = %s"
    data = (105, 'sarita', 72, 72, 26, 1)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate3(rollNo, name, phy, chm, maths, id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "update marksheet set rollNo = %s, name = %s, phy = %s, chm = %s, maths = %s where id = %s"
    data = (rollNo, name, phy, chm, maths, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate4(data):
    id = data['id']
    rollNo = data['rollNo']
    name = data['name']
    phy = data['phy']
    chm = data['chm']
    maths = data['maths']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "update marksheet set rollNo = %s, name = %s, phy = %s, chm = %s, maths = %s where id = %s"
    data = (rollNo, name, phy, chm, maths, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')

# testUpdate1()
# testUpdate2()
# testUpdate3(103, 'pqr', 89, 77, 67, 3)

params = {}
params['id'] = 8
params['rollNo'] = 104
params['name'] = 'Raju'
params['phy'] = 65
params['chm'] = 79
params['maths'] = 80

testUpdate4(params)