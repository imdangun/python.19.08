x=10
def foo():
    print(x)

foo() # 10
print(x) # 10
##

def foo():
    y=10
    print(y)

foo() # 10
print(y) # NameError: name 'y' is not defined
##

x=1
def foo():
    x=2
    print(x)

foo() # 2
print(x) # 1

x=10
def foo():
    global x
    x=20
    print(x)

foo()  # 20
print(x) # 20
##

def hello():
    hello = 'hello world'
    def msg():
        print(hello)
    msg()

hello() # hello world
##

def A():
    x=10
    def B():
        x=20
    B()
    print(x)

A() # 10


def A():
    x=10
    def B():
        nonlocal x
        x=20
    B()
    print(x)

A() # 20
##

def A():
    x=10
    y=100
    def B():
        x=20
        def C():
            nonlocal x
            nonlocal y
            x=x+30
            y=y+30
            print(x)
            print(y)
        C()
    B()

A()
'''
50
130
'''
##

x=1
def A():
    x=10
    def B():
        x=20
        def C():
            global x
            x=x+30
            print(x)
        C()
    B()

A() # 31
##

def calc():
    a=3
    b=5
    def mulAdd(x):
        return x*a+b
    return mulAdd

c = calc()
print(c(1),c(2),c(3)) # 8 11 14
##

def calc():
    a=3
    b=5
    return lambda x:a*x+b

c=calc()
print(c(1),c(2),c(3)) # 8 11 14
##

def calc():
    a=1
    b=10
    total=0
    def mulAdd(x):
        nonlocal total
        total=a*x+b+total
        print(total)
    return mulAdd

c=calc()
c(1),c(2),c(3)
'''
11
23
36
(None, None, None)
'''