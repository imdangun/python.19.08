class Person:
    def greet(self):
        print('hello')

james = Person()
james.greet() # hello
##

int(10)
a=list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dict(x=10, y=20) # {'x': 10, 'y': 20}

a.append(20)
a # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
##

type(10) # <class 'int'>
type([0,1]) # <class 'list'>
type({'x':0, 'y':1}) # <class 'dict'>
type(Person()) # <class '__main__.Person'>
##

class Person:
    pass

class Person:
    def greet(self):
        print('hello')

    def hello(self):
        self.greet()

james = Person()
james.hello() # hello

isinstance(james, Person) # True
##

class Person:
    def __init__(self):
        self.hello='안녕'

    def greet(self):
        print(self.hello)

james = Person()
james.greet() # 안녕
##

class Person:
    def __init__(self, name, age):
        self.hello = '안녕'
        self.name = name
        self.age = age

    def greet(self):
        print('{0} 저는 {1}살 {2}입니다.'.format(self.hello, self.age, self.name))

person = Person('한아름',67)
person.greet() # 안녕 저는 67살 한아름입니다.

person.name # '한아름'
person.age  # 67
##

class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]

    def greet(self):
        print('{0}: {1}살'.format(self.name, self.age))

person = Person(*['박혁세',27])
person.greet() # 박혁세: 27살
##

class Person:
    def __init__(self, **args):
        self.name = args['name']
        self.age = args['age']

    def greet(self):
        print(self.name, ': ', self.age, '살')

person1 = Person(name='최한석', age=12)
person1.greet() # 최한석 :  12 살

person2 = Person(**{'name':'한아름', 'age':27})
person2.greet() # 한아름 :  27 살

person1.address='서울'
person1.address # '서울'
person2.address # 'Person' object has no attribute 'address'
##

class Person:
    def __init__(self, name, money):
        self.name = name
        self.__money = money # private attribute

person = Person('양승일',2000)
person.name # '양승일'
person.money # 'Person' object has no attribute 'money'
##

class Person:
    def __init__(self, name, money):
        self.name = name
        self.__money = money

    def pay(self, money):
        self.__money -= money
        print('{0}만 원 지불, {1}만 원 잔액.'.format(money, self.__money))

person = Person('김보라',7000)
person.pay(3000) # 3000만 원 지불, 4000만 원 잔액.
##

class Person:
    def __sing(self):
        print('라라라')

    def hello(self):
        print('안녕')

    def show(self):
        self.__sing()

person = Person()
person.__sing() # 'Person' object has no attribute '__sing'
person.hello() # 안녕
person.show() # 라라라