x={'a':1, 'b':2, 'c':3}
x.setdefault('e') # {'a': 1, 'b': 2, 'c': 3, 'e': None}
x.setdefault('f',100) # {'a': 1, 'b': 2, 'c': 3, 'e': None, 'f': 100}

x={'a':1, 'b':2}
x.update(a=90) # {'a': 90, 'b': 2}
x.update(c=10) # {'a': 90, 'b': 2, 'c': 10}
x.update(c=100, d=200) # {'a': 90, 'b': 2, 'c': 100, 'd': 200}
x.update({'a':7, 'b':8}) # {'a': 7, 'b': 8, 'c': 100, 'd': 200}

x={1:'one', 2:'two'}
x.update([[2,'two'],[3,'three']]) # {1: 'one', 2: 'two', 3: 'three'}
x.update(zip([3,4],['three','four'])) # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

x={1:'one', 2:'two'}
x.setdefault(1,'하나') # {1: 'one', 2: 'two'} 추가O, 수정X
x.update({1:'하나'}) # {1: '하나', 2: 'two'}   추가O, 수정O

x={'name':'최한석', 'age':12}
x.pop('name') # '최한석', {'age': 12}
x.pop('x',0) # 0
del x['age'] # {}

x={'a':1, 'b':2, 'c':3}
x.popitem() # ('c', 3), {'a': 1, 'b': 2}
x.clear() # {}

x = {'a':1, 'b':2, 'c':3}
x.get('a') # 1
x.get('x', 0) # 0
x.items() # dict_items([('a', 1), ('b', 2), ('c', 3)])
x.keys() # dict_keys(['a', 'b', 'c'])
x.values() # dict_values([1, 2, 3])

keys=['a','b','c']
x=dict.fromkeys(keys) # {'a': None, 'b': None, 'c': None}
x=dict.fromkeys(keys,100) # {'a': 100, 'b': 100, 'c': 100}
##

x={'a':1, 'b':2, 'c':3}
for i in x:
    print(i, end=' ') # a b c

for key, value in x.items():
    print(key, value)
'''
a 1
b 2
c 3
'''
##

x={'a':1, 'b':2, 'c':3}
for key in x.keys():
    print(key, end=' ') # a b c

for value in x.values():
    print(value, end=' ') # 1 2 3

keys=['a','b','c']
x={key:value for key,value in dict.fromkeys(keys).items()}
# {'a': None, 'b': None, 'c': None}

{key:0 for key in dict.fromkeys(['a','b','c']).keys()}
# {'a': 0, 'b': 0, 'c': 0}

{value:key for key,value in {'a':1, 'b':2, 'c':3}.items()}
# {1: 'a', 2: 'b', 3: 'c'}
##

x={'a':1, 'b':2, 'c':3}
for key,value in x.items():
    if value == 2:
        del x[key]
# {'a': 1, 'c': 3}
# RuntimeError: dictionary changed size during iteration

x={'a':1, 'b':2, 'c':3}
x={key:value for key,value in x.items() if value != 20}
# {'a': 1, 'b': 2, 'c': 3}
##

x={'a':1, 'b':2, 'c':3}
y=x
x is y # True
y['a'] # 1
y['a']=99 # x={dict}{'a': 99, 'b': 2, 'c': 3}

x={'a':1, 'b':2, 'c':3}
y=x.copy()
x is y # False
x == y # True
y['a']=99 # x={dict}{'a': 99, 'b': 2, 'c': 3}
##

x={'a':{'python':'2.7'}, 'b':{'python':'3.6'}}
y=x.copy()
y['a']['python']='2.7.15'
print(x) # {'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}
print(y) # {'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}

x={'a':{'python':'2.7'}, 'b':{'python':'3.6'}}
import copy
y=copy.deepcopy(x)
y['a']['python']='2.7.15'
print(x) # {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
print(y) # {'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}