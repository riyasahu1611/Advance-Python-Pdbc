import pymysql


def testFunction():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    cursor.execute('select square(7)')
    result = cursor.fetchall()
    print(result[0][0])
    connection.close()


testFunction()

