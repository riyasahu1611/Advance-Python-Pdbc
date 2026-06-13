from MarksheetModel import MarksheetModel

def testAdd():
    params = {}
    params['id'] = 20
    params['rollNo'] = 108
    params['name'] = 'abc'
    params['phy'] = 70
    params['chm'] = 70
    params['maths'] = 70

    model = MarksheetModel()
    model.add(params)

def testUpdate():
    params = {}
    params['id'] = 9
    params['rollNo'] = 106
    params['name'] = 'Akriti'
    params['phy'] = 80
    params['chm'] = 85
    params['maths'] = 90

    model = MarksheetModel()
    model.update(params)


def testDelete():
    model = MarksheetModel()
    model.delete(8)


def testGet():
    model = MarksheetModel()
    result = model.get(1)
    for data in result:
        print(data['id'], '\t', data['rollNo'], '\t', data['name'], '\t', data['phy'], '\t', data['chm'], '\t', data['maths'])


def testFindByRoll():
    model = MarksheetModel()
    result = model.FindByRoll(105)
    for data in result:
        print(data['id'], '\t', data['rollNo'], '\t', data['name'], '\t', data['phy'], '\t', data['chm'], '\t', data['maths'])


def testSearch():
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 0

    model = MarksheetModel()
    result = model.search(params)
    for data in result:
        print(data['id'], '\t', data['rollNo'], '\t', data['name'], '\t', data['phy'], '\t', data['chm'], '\t', data['maths'])

# testAdd()
testUpdate()
# testDelete()
# testRead()
# testGet()
# testFindByRoll()
# testSearch()