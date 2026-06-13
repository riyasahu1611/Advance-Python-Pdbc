import pymysql

class RoleModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
        cursor = connection.cursor()
        sql = "select max(id) from role"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, data):
        id = RoleModel.next_pk(self)
        name = data['name']
        description = data['description']

        user_exist = self.test_find_by_name(name)

        if len(user_exist) > 0 and user_exist[0].get('id') != id:
            raise Exception('name already exist')

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
        cursor = connection.cursor()
        sql = "insert into role values(%s, %s, %s)"
        data = (id, name, description)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data['id']
        name = data['name']
        description = data['description']

        role_exist = self.test_find_by_name(name)

        if len(role_exist) > 0 and role_exist[0].get('id') != id:
            raise Exception('name already exist')

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
        cursor = connection.cursor()
        sql = "update role set name = %s, description = %s where id = %s"
        data = (name, description, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')

    def delete(self, name):
        user_exist = self.test_find_by_name(name)

        if len(user_exist) > 0 and user_exist[0].get('id') != id:
            raise Exception('name does not exist')

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
        cursor = connection.cursor()
        sql = "delete from role where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
        cursor = connection.cursor()
        sql = "select * from role where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "name", "description")
        res = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res


    def test_find_by_name(self, name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
        cursor = connection.cursor()
        sql = "select * from role where name = %s"
        data = (name,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "name", "description")
        res = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res


    def search(self, data):
        id = data.get('id', 0)
        name = data.get('name', '')
        description = data.get('description', '')
        pageNo = data.get('pageNo', 0)
        pageSize = data.get('pageSize', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advpython')
        cursor = connection.cursor()
        sql = "select * from role where 1=1"
        if id != 0:
            sql += " and id = " + str(id)
        if name != '':
            sql += " and name like '" + name + "%'"
        if description != '':
            sql += " and description like '" + description + "%'"
        if pageSize > 0:
            pageNo = (pageNo - 1) * pageSize
            sql += " limit " + str(pageNo) + ", " + str(pageSize)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        columnName = ("id", "name", "description")
        res = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res





