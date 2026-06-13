from MarksheetModel import MarksheetModel

def testAdd():
    params = {}
    params['id'] = 21
    params['rollNo'] = 208
    params['name'] = 'xyz'
    params['phy'] = 70
    params['chm'] = 70
    params['maths'] = 70

    model = MarksheetModel()
    try:
        model.update(params)
    except Exception as e:
        print('exception:', e)

def testUpdate():
    params = {}
    params['id'] = 7
    params['rollNo'] = 206
    params['name'] = 'Akriti'
    params['phy'] = 80
    params['chm'] = 85
    params['maths'] = 90

    model = MarksheetModel()
    try:
        model.update(params)
    except Exception as e:
        print('exception:', e)


def testDelete():
    model = MarksheetModel()
    try:
        model.delete(5)
    except Exception as e:
        print('exception:', e)


def testGet():
    model = MarksheetModel()
    try:
        result = model.get(300)
        print(result)
    except Exception as e:
        print('exception:', e)


def Find_By_Roll():
    model = MarksheetModel()
    try:
        result = model.get(105)
        print(result)
    except Exception as e:
        print('exception:', e)

def testSearch():
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 0

    model = MarksheetModel()
    result = model.search(params)
    for data in result:
        print(data['id'], '\t', data['rollNo'], '\t', data['name'], '\t', data['phy'], '\t', data['chm'], '\t', data['maths'])

# testAdd()
# testUpdate()
# testDelete()
# testRead()
# testGet()
Find_By_Roll()
# testSearch()