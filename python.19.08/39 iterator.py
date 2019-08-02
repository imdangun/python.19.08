dir([1,2,3]) # [... '__init_subclass__', '__iter__', '__le__' ...]

it = [1,2,3].__iter__() # <list_iterator object at 0x03202E30>
it.__next__() # 1
it.__next__() # 2
it.__next__() # 3
it.__next__() # StopIteration

'hello'.__iter__() # <str_iterator object at 0x03271FF0>
{'a':1, 'b':2}.__iter__() # <dict_keyiterator object at 0x03279B70>
{1,2}.__iter__() # <set_iterator object at 0x031BD7D8>

it = range(3).__iter__()
it.__next__() # 0
it.__next__() # 1
it.__next__() # 2
it.__next__() # StopIteration
##

class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration

for i in Counter(3):
    print(i, end=' ')
'''
0 1 2 
'''
##

# iterator unpacking
a,b,c = Counter(3)
a,b,c # (0, 1, 2)

a,_,c,d = range(4)
a,c,d # (0, 2, 3)
##

class Counter:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, idx):
        if idx < self.stop:
            return idx
        else:
            raise IndexError

Counter(3)[1], Counter(3)[0], Counter(3)[2] # (1, 0, 2)
##

it = iter(range(3))
next(it) # 0
next(it) # 1
next(it) # 2
next(it) # StopIteration
##

import random
it = iter(lambda: random.randint(0,5),2) # iter(callable, sentinel)
next(it) # 2
next(it) # 1
next(it) # 3
next(it) # 1
next(it) # 5
next(it) # StopIteration
next(it) # StopIteration
##

for i in iter(lambda:random.randint(0,5),2):
    print(i, end=' ')
'''
0 1 4 1 
'''
##

it = iter(range(3))
next(it, 10) # 0
next(it, 10) # 1
next(it, 10) # 2
next(it, 10) # 10
next(it, 10) # 10