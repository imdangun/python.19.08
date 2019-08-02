def hello():
    print('hello')

hello() # 'hello'
##

def add(a,b):
    """ 숫자 2개를 더한다. """
    print(a+b)

add(1,3) # 4

print(add.__doc__)
##

def add(a,b):
    return a+b

add(1,2) # 3
##

def add_sub(a,b):
    return a+b, a-b
x,y=add_sub(1,2)
x # 3
y # -1

x = add_sub(1,2)
x # (3, -1)
##

def num():
    return (1,2)

def num2():
    return 1,2

def num3():
    return [1,2]

num() # (1,2)
num2() # (1,2)
num3() # [1, 2]
##

def mul(a,b):
    c=a*b
    return c

def add(a,b):
    c=a+b
    print(c)
    d = mul(a,b)
    print(d)
x=1
y=2
add(1,2)
'''
3
2
'''