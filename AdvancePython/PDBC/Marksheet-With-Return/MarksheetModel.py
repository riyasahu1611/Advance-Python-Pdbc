import pymysql

class MarksheetModel:

    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
        cursor = connection.cursor()
        sql = "select max(id) from marksheet"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        print(pk + 1)

    def add(self, data):
        id = MarksheetModel.nextPk(self)
        rollNo = data['rollNo']
        name = data['name']
        phy = data['phy']
        chm = data['chm']
        maths = data['maths']

        user_exist = self.Find_By_Roll(rollNo)

        if len(user_exist) > 0:
            raise Exception('Roll No already exist')

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
        cursor = connection.cursor()
        sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
        data = (id, rollNo, name, phy, chm, maths)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data['id']
        rollNo = data['rollNo']
        name = data['name']
        phy = data['phy']
        chm = data['chm']
        maths = data['maths']

        user_exist = self.Find_By_Roll(rollNo)

        if len(user_exist) > 0:
            raise Exception('Roll No already exist')

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
        cursor = connection.cursor()
        sql = "update marksheet set rollNo = %s, name = %s, phy = %s, chm = %s, maths = %s where id = %s"
        data = (rollNo, name, phy, chm, maths, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
        cursor = connection.cursor()
        sql = "delete from marksheet where id = %s"
        data = (id)
        cursor.execute(sql, data)

        user_exist = self.Find_By_Roll(id)

        if len(user_exist) > 0:
            raise Exception('Roll No already exist')

        connection.commit()
        connection.close()
        print('data deleted successfully')

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
        cursor = connection.cursor()
        sql = "select * from marksheet where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()

        user_exist = self.Find_By_Roll(id)

        if len(user_exist) == 0:
            raise Exception('Id does not exist')

        columnName = ("id", "rollNo", "name", "phy", "chm", "maths")
        res = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res


    def Find_By_Roll(self, rollNo):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
        cursor = connection.cursor()
        sql = "select * from marksheet where rollNo = %s"
        data = (rollNo,)
        cursor.execute(sql, data)
        result = cursor.fetchall()

        user_exist = self.Find_By_Roll(rollNo)

        if len(user_exist) > 0:
            raise Exception('Roll No already exist')

        columnName = ("id", "rollNo", "name", "phy", "chm", "maths")
        res = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res


    def search(self, data):
        id = data.get('id', 0)
        rollNo = data.get('rollNo', 0)
        name = data.get('name', '')
        phy = data.get('phy', 0)
        chm = data.get('chm', 0)
        maths = data.get('maths', 0)
        pageNo = data.get('pageNo', 0)
        pageSize = data.get('pageSize', 0)

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
        columnName = ("id", "rollNo", "name", "phy", "chm", "maths")
        res = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res
