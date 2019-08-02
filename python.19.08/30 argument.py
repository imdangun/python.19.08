print(1,2,3) # 1 2 3, positional argument
##

def printNum(a,b,c):
    print(a)
    print(b)
    print(c)

printNum(1,2,3)
'''
1
2
3
'''

x=[1,2,3]
printNum(*x) # unpacking
'''
1
2
3
'''

printNum(*[1,2,3])
'''
1
2
3
'''
##

def printNums(*args):
    for arg in args:
        print(arg)

printNums(1) # 1
printNums(1,2,3)
'''
1
2
3
'''

x = [10]
printNums(*x) # 10
x = [1,2,3]
printNums(*x)
'''
1
2
3
'''
##

def printNums(a, *args):
    print(a)
    print(args)

printNums(1)
'''
1
()
'''

printNums(1,2,3)
'''
1
(2, 3)
'''

printNums(*[1,2,3])
'''
1
(2, 3)
'''
##

def person(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

person('최한석',25,'서울 서초구 반포동')
'''
이름:  최한석
나이:  25
주소:  서울 서초구 반포동
'''
# keyword arguments
person(name='한아름',age=35,address='서울 용산구 이촌동')
'''
이름:  한아름
나이:  35
주소:  서울 용산구 이촌동
'''

person(age=35,address='서울 용산구 이촌동',name='한아름')
'''
이름:  한아름
나이:  35
주소:  서울 용산구 이촌동
'''

# dictionary unpacking
x={'name':'최한석', 'age':30, 'address':'서울 은평구 불광동'}
person(**x)
'''
이름:  최한석
나이:  30
주소:  서울 은평구 불광동
'''

person(**{'name':'최한석', 'age':30, 'address':'서울 은평구 불광동'})
'''
이름:  최한석
나이:  30
주소:  서울 은평구 불광동
'''

person(*x)
'''
이름:  name
나이:  age
주소:  address
'''
##

def person(**args):
    for key,value in args.items():
        print(key,':',value,sep='')

person(name='최한석') # name:최한석
person(**{'name':'한아름'}) # name:한아름
person(**{'name':'최한석', 'age':30, 'address':'서울 은평구 불광동'})
'''
name:최한석
age:30
address:서울 은평구 불광동
'''
##

def person(**args):
    if 'name' in args:
        print('이름',':',args['name'])
    if 'age' in args:
        print('나이',':',args['age'])

person(**{'name':'김보라', 'address':'서울'}) # 이름 : 김보라
##

def person(name, **args):
    print(name)
    print(args)

person('최한석')
'''
최한석
{}
'''

person('한아름', age=57, address='인천')
'''
한아름
{'age': 57, 'address': '인천'}
'''

person(**{'name':'양승일', 'age':30, 'address':'광주'})
'''
양승일
{'age': 30, 'address': '광주'}
'''
##

def person(name, age, address='서울'):
    print(name)
    print(age)
    print(address)

person('김보라',27)
'''
김보라
27
서울
'''

person('박혁세',56,'부산')
'''
박혁세
56
부산
'''