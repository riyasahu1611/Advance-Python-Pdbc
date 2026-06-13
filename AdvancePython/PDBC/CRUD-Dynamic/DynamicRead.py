import pymysql


def testRead1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "select * from marksheet"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "select * from marksheet"
    cursor.execute(sql)
    result = cursor.fetchall()
    columnName = ("id", "rollNo", "name", "phy", "chm", "maths")
    for x in result:
        print({columnName[i]: x[i] for i, _ in enumerate(x)})
    connection.commit()
    connection.close()


def testRead3():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "select * from marksheet"
    sql = "select * from marksheet WHERE id = 1"
    sql = "select * from marksheet WHERE rollNo = 105"
    sql = "select * from marksheet WHERE name = 's%'"
    sql = "select * from marksheet WHERE phy = 72"
    sql = "select * from marksheet WHERE chm = 72"
    sql = "select * from marksheet WHERE maths = 26"
    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead4(id, rollNo, name, phy, chm, maths):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()

    sql = 'select * from marksheet'
    if id != 0:
        sql += " where id = " + str(id)
    if rollNo != 0:
        sql += " where roll_no = " + str(rollNo)
    if name != '':
        sql += " where name like '" + name + "%'"
    if phy != 0:
        sql += " where physics = " + str(phy)
    if chm != 0:
        sql += " where chemistry = " + str(chm)
    if maths != 0:
        sql += " where maths = " + str(maths)
    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()

def testRead5(param={}):
    id = param.get('id', 0)
    rollNo = param.get('rollNo', 0)
    name = param.get('name', '')
    phy = param.get('phy', 0)
    chm = param.get('chm', 0)
    maths = param.get('maths', 0)

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "select * from marksheet where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if rollNo != 0:
        sql += " and rollNo = " + str(rollNo)
    if name != '':
        sql += " and name like '" + name + "%'"
    if phy != 0:
        sql += " and physics = " + str(phy)
    if chm != 0:
        sql += " and chemistry = " + str(chm)
    if maths != 0:
        sql += " and maths = " + str(maths)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead6(param={}):
    id = param.get('id', 0)
    rollNo = param.get('rollNo', 0)
    name = param.get('name', '')
    phy = param.get('phy', 0)
    chm = param.get('chm', 0)
    maths = param.get('maths', 0)
    pageNo = param.get('pageNo', 0)
    pageSize = param.get('pageSize', 0)

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "select * from marksheet where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if rollNo != 0:
        sql += " and rollNo = " + str(rollNo)
    if name != '':
        sql += " and name like '" + name + "%'"
    if phy != 0:
        sql += " and phy = " + str(phy)
    if chm != 0:
        sql += " and chm = " + str(chm)
    if maths != 0:
        sql += " and maths = " + str(maths)

    if pageSize > 0:
        pageNo = (pageNo - 1) * pageSize
        sql += " limit " + str(pageNo) + ", " + str(pageSize)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()
param = {}
param['name'] = 's'
param['phy'] = 72
param['rollNo'] = 105
param['pageNo'] = 1
param['pageSize'] = 5

# testRead1()
# testRead2()
# testRead3()
# testRead4(1,10, '', 0, 0, 0)
# testRead5(param)
testRead6(param)


