import pymysql

def testRead5(param={}):
    id = param.get('id', 0)
    name = param.get('name', '')
    address = param.get('address', '')

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    sql = "select * from student where 1=1"      #1=1 sql injection - append 2 queries at run time
    if id != 0:
        sql += " and id = " + str(id)
    if name != '':
        sql += " and name like '" + name + "%'"
    if address != '':
        sql += " and address like '" + address + "%'"

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2])
    connection.commit()
    connection.close()


def testRead6(param={}):
    id = param.get('id', 0)
    name = param.get('name', '')
    address = param.get('address', '')
    pageNo = param.get('pageNo', 0)
    pageSize = param.get('pageSize', 0)

    connection = pymysql.connect(
        host='localhost', port=3306, user='root', password='root', database='advpython'
    )
    cursor = connection.cursor()

    sql = "SELECT * FROM student WHERE 1=1"
    if id != 0:
        sql += " AND id = " + str(id)
    if name != '':
        sql += " AND name LIKE '" + name + "%'"
    if address != '':
        sql += " AND address LIKE '" + address + "%'"

    # Pagination
    if pageSize > 0:
        offset = (pageNo - 1) * pageSize
        sql += " LIMIT " + str(offset) + ", " + str(pageSize)

    print('sql =>', sql)

    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2])

    connection.commit()
    connection.close()


param = {'id': 0,
         'name': 'Aman',
         'address': '',
         'pageNo': 2,
         'pageSize': 2
         }
# testRead5(param)
testRead6(param)
