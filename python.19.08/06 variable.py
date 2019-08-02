x=10
x # 10

x, y, z = 10, 20, 30
x, y, z # (10, 20, 30)

x, y = y, x
x, y # (20, 10)

del x
x # NameError: name 'x' is not defined

x = None
x # (출력 되는 것이 없다.)

a=10
b=20
c=a+b
c # 30

a = 10
a = a+20
a # 30

a = 10
a += 20
a # 30

input() # >? hello, 'hello'
input() # >? 1, '1'
x = input()
x # 'world'

x = input('문자열을 입력하세요.') # 문자열을 입력하세요.>? great
x # 'great'

a = input('숫자 1') # 숫자 1>? 10
b = input('숫자 2') # 숫자 2>? 20
print(a+b) # 1020s
type(a) # <class 'str'>

a = int(input('숫자1')) # 숫자1>? 1
b = int(input('숫자2')) # 숫자2>? 2
print(a+b) # 3

a, b = input('두개 입력하세요.').split() # 두개 입력하세요.>? hello world
a, b # ('hello', 'world')

a, b = input('숫자 2개 입력하세요.').split() # 숫자 2개 입력하세요.>? 1 2
a = int(a)
b = int(b)
print(a+b) # 3

a, b = input('숫자 2개 입력하세요.').split() # 숫자 2개 입력하세요.>? 1 2
print(int(a)+int(b)) # 3

a, b = map(int, input('숫자 2개 입력하세요.').split()) # 숫자 2개 입력하세요.>? 1 2
print(a+b) # 3
a, b = map(int, input('숫자 2개 입력하세요.').split(',')) # 숫자 2개 입력하세요.>? 1,2
print(a+b) # 3

