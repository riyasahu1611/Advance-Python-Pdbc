from role_model import RoleModel

def add():
    params = {}
    params['id'] = 8
    params['name'] = 'Raj Sharma'
    params['description'] = 'Hr'

    model = RoleModel()
    try:
        model.update(params)
    except Exception as e:
        print('exception:', e)

def update():
    params = {}
    params['id'] = 1
    params['name'] = 'Riya Sahu'
    params['description'] = 'Admin'

    model = RoleModel()
    try:
        model.update(params)
    except Exception as e:
        print('exception:', e)


def testDelete():
    model = RoleModel()
    try:
        model.delete(2)
    except Exception as e:
        print('exception:', e)

def testGet():
    model = RoleModel()
    try:
        model.get(1)
    except Exception as e:
        print('exception:', e)


def test_find_by_name():
    model = RoleModel()
    try:
        model.test_find_by_name('Riya Sahu')
    except Exception as e:
        print('exception:', e)


def search():
    params = {}
    params['id']= 0
    params['name'] = ''
    params['description']= ''
    params['pageNo'] = 1
    params['pageSize'] = 2

    model = RoleModel()
    try:
        model.search('Riya Sahu')
    except Exception as e:
        print('exception:', e)

# add()
update()
# testDelete()
# testGet()
# test_find_by_name()
# search()