class Person:
    def greet(self):
        print('안녕')

class Student(Person):
    def study(self):
        print('공부하다.')

student1 = Student()
student1.study() # 공부하다.
student1.greet() # 안녕

issubclass(Student, Person) # True
##

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello='안녕'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school='서울대학교'

student = Student() # Student __init__
student.school # '서울대학교'
student.hello # 'Student' object has no attribute 'hello'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()
        self.school='연세대학교'

student = Student()
'''
Student __init__
Person __init__
'''
student.school # '연세대학교'
student.hello # '안녕'
##

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello='안녕'

class Student(Person):
    pass

student = Student() # Person __init__
student.hello # '안녕'
##

# overriding
class Person:
    def say(self):
        print('사람')

class Student(Person):
    def say(self):
        super().say()
        print('학생')

student = Student()
student.say()
'''
사람
학생
'''
##

# diamond inheritance
class Person:
    def greet(self):
        print('안녕')

class Undergraduate:
    def manageCredit(self):
        print('학점 관리하다.')

class Student(Person, Undergraduate):
    def study(self):
        print('공부하다.')

student = Student()
student.study() # 공부하다.
student.manageCredit() # 학점 관리하다.
student.greet() # 안녕
##

class Person:
    def greet(self):
        print('안녕')

class Undergraduate(Person):
    def manageCredit(self):
        print('학점 관리하다.')

class Student(Undergraduate):
    def study(self):
        print('공부하다.')

student = Student()
student.study() # 공부하다.
student.manageCredit() # 학점 관리하다.
student.greet() # 안녕
##

# MRO(Method Resolution Order)
int.mro() # [<class 'int'>, <class 'object'>]

class A:
    pass
A.mro() # [<class '__main__.A'>, <class 'object'>]

class A(object):
    pass
A.mro() # [<class '__main__.A'>, <class 'object'>]
##

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def goToSchool(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하다.')

student = Student()
# Can't instantiate abstract class Student with abstract methods goToSchool

class Student(StudentBase):
    def study(self):
        print('공부하다.')

    def goToSchool(self):
        print('학교 가다.')

student = Student()