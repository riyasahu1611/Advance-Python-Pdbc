from user_model import UserModel
import datetime


def add():
    params = {}
    params['first_name'] = 'Ritika'
    params['last_name'] = 'Sharma'
    params['login_id'] = '106Ritika'
    params['password'] = 'abc1234'
    params['dob'] = datetime.date(2002, 11, 27)
    params['address'] = 'Ujjain'

    model = UserModel()
    try:
        model.add(params)
    except Exception as e:
        print('exception:', e)

def update():
    params = {}
    params['first_name'] = 'Raj'
    params['last_name'] = 'Sharma'
    params['login_id'] = 'raj@gmail.com'
    params['password'] = '12345'
    params['dob'] = datetime.date(2002, 12, 27)
    params['address'] = 'Indore'
    params['id'] = 4

    model = UserModel()
    try:
        model.update(params)
    except Exception as e:
        print('exception:', e)


# add()
update()