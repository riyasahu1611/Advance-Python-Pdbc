import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='rays',
                             autocommit=False)

cursor = connection.cursor()

try:
    print("Starting transaction...")
    cursor.execute("insert into marksheet values(25, 116, 'rahul', 13, 48, 38)")

    print("Creating savepoint sp1...")
    cursor.execute("savepoint sp1")

    try:
        cursor.execute("insert into marksheet values(26, 120, 'anmol', 13, 48, 38)")
        print("Creating savepoint sp2...")
        cursor.execute("savepoint sp2")
    except Exception as e:
        print("Error in second insert, rolling back to savepoint sp1...")
        cursor.execute("rollback to savepoint sp1")

    try:
        cursor.execute("insert into marksheet values(24, 116, 'rahul', 13, 48, 38)")
        print("Second insert successful.")
        print("Creating savepoint sp3...")
        cursor.execute("savepoint sp3")
    except Exception as e:
        print("Error in third insert, rolling back to savepoint sp1...")
        cursor.execute("rollback to savepoint sp1")

    print("Committing transaction...")
    connection.commit()

except Exception as e:
    print("Error in transaction:", e)
    connection.rollback()

finally:
    cursor.close()
    connection.close()
