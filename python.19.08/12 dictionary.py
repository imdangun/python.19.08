person = {'name':'최한석', 'age':25}
person['name'] # '최한석'

# key type: str, int, float, boolean
x = {1:'최한석', 2:'한아름',False:0, True:1, 3.5:[3.5,3.5]}

x = {}
x = dict()

person = dict(name='최한석', age=25) # {'name': '최한석', 'age': 25}
person = dict(zip(['name','age'],['최한석',25])) # {'name': '최한석', 'age': 25}
person = dict([('name','최한석'),('age',25)]) # {'name': '최한석', 'age': 25}
person = dict({'name':'최한석', 'age':25})

person['name'] = '양승일' # {'name': '양승일', 'age': 25}
person['age'] = 35 # {'name': '양승일', 'age': 35}
person['regDate'] = '12/20' # {'name': '양승일', 'age': 35, 'regDate': '12/20'}

'name' in person # True
'name' not in person # False

len(person) # 3