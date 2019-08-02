class Person:
    bag = [] # class attribute

    def put(self, stuff):
        Person.bag.append(stuff)

    def openBag(self):
        print(Person.bag)

person1 = Person()
person1.put('책')

person2 = Person()
person2.put('가위')
person2.openBag() # ['책', '가위']

person2.__dict__ # {}
Person.__dict__ # ... 'bag': ['책', '가위'], ...
##

class Person:
    def __init__(self):
        self.bag = [] # instance attribute

    def put(self, stuff):
        self.bag.append(stuff)

    def openBag(self):
        print(self.bag)

person1 = Person()
person1.put('사과')

person2 = Person()
person2.put('바나나')
person2.openBag() # ['바나나']

person1.openBag() # ['사과']
##

class Person:
    '''사람 클래스'''
    def greet(self):
        '''인사'''
        print('hello')

print(Person.__doc__) # 사람 클래스
print(Person.greet.__doc__) # 인사

person = Person()
print(person.greet.__doc__) # 인사
##

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def mul(a,b):
        print(a*b)

Calc.add(10,20) # 30
Calc.mul(10,20) # 200
##

class Person:
    cnt = 0

    def __init__(self):
        Person.cnt += 1

    @classmethod
    def printCnt(cls):
        print('{0}명 생성.'.format(cls.cnt))

    @classmethod
    def birth(cls):
        return cls()

person1 = Person()
person2 = Person()
person3 = Person.birth()

Person.printCnt() # 3명 생성.
##

class Person:
    cnt = 0

    def __init__(self):
        Person.cnt += 1

    @staticmethod
    def printCnt(cls):
        print('{0}명 생성.'.format(cls.cnt))

person1 = Person()
person2 = Person()

Person.printCnt() # 2명 생성.
# printCnt() missing 1 required positional argument: 'cls'