def numGenerator():
    yield 0
    yield 1
    yield 2

for i in numGenerator():
    print(i, end=' ')
'''
0 1 2
'''
##

g=dir(numGenerator()) # [...'__init_subclass__', '__iter__', '__le__',...]
##

g=numGenerator()
g.__next__() # 0
g.__next__() # 1
g.__next__() # 2
g.__next__() # StopIteration
##

def numGenerator(stop):
    n = 0
    while n<stop:
        yield n
        n += 1

for i in numGenerator(3):
    print(i, end=' ')
'''
0 1 2 
'''
##

def upperChar(x):
    for i in x:
        yield i.upper()

fruits=['apple','pear']

for i in upperChar(fruits):
    print(i, end=' ')
'''
APPLE PEAR 
'''
##

def numGenerator():
    x=[1,2,3]
    for i in x:
        yield i

for i in numGenerator():
    print(i, end=' ')
'''
1 2 3 
'''
##

def nums():
    x=[1,2,3]
    yield from x # yield from iterable object

for i in nums():
    print(i, end=' ')
'''
1 2 3 
'''
##

def numGenerator(stop):
    n=0
    while n<stop:
        yield n
        n += 1

def nums():
    yield from numGenerator(3) # yeild from generator

for i in nums():
    print(i, end=' ')
'''
0 1 2
'''
##

[i for i in range(50) if i%2==0] # [[0, 2, 4, 6,...]
(i for i in range(50) if i%2==0) # <generator object <genexpr> at 0x032803B0>
