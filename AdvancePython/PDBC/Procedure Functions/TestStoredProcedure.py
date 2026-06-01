import pymysql

def emprIn():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    cursor.callproc('emprIn', [2])
    results = cursor.fetchall()
    for row in results:
        print(row)
    connection.close()

def emprOut():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    cursor.execute('CALL emprOut(@output)')
    cursor.execute("SELECT @output")
    result = cursor.fetchall()
    print(result[0][0])
    connection.close()

def emprInOut():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
    cursor = connection.cursor()
    cursor.execute('SET @input_output = 5')
    cursor.execute('CALL emprInOut(@input_output)')
    cursor.execute("SELECT @input_output")
    result = cursor.fetchone()
    print(result[0])
    connection.close()

# emprIn()
# emprOut()
emprInOut()