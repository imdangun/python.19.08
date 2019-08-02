def hello():
    print('hello() 시작.')
    print('hello')
    print('hello() 끝.')

def world():
    print('world() 시작.')
    print('world')
    print('world() 끝.')

hello()
'''
hello() 시작.
hello
hello() 끝.
'''
world()
'''
world() 시작.
world
world() 끝.
'''
##

def trace(func):
    def wrapper():
        print(func.__name__,'시작')
        func()
        print(func.__name__,'끝')
    return wrapper

def hello():
    print('hello')

def world():
    print('world')

traceHello = trace(hello)
traceHello()
'''
hello 시작
hello
hello 끝
'''
traceWorld = trace(world)
traceWorld()
'''
world 시작
world
world 끝
'''
##

@trace
def hello():
    print('hello')

@trace
def world():
    print('world')

hello()
'''
hello 시작
hello
hello 끝
'''

world()
'''
world 시작
world
world 끝
'''
##

def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper

@decorator1
@decorator2
def hello():
    print('hello')

hello()
'''
decorator1
decorator2
hello
'''
##

def trace(func):
    def wrapper(a,b):
        r = func(a,b)
        return r
    return wrapper

@trace
def add(a,b):
    return a+b

add(1,2) # 3

