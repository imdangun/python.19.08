fruits={'orange','cherry','berry'}
fruits # {'cherry', 'berry', 'orange'}

fruits={'orange','orange','berry'}
fruits # {'berry', 'orange'}

'orange' in fruits # True
'peach' in fruits # False
'peach' not in fruits # True

set('apple') # {'p', 'l', 'e', 'a'}
set('안녕') # {'안', '녕'}
set(range(5)) # {0, 1, 2, 3, 4}
set() # set()

c = {}
type(c) # <class 'dict'>
c = set()
type(c) # <class 'set'>
##

a = {1,2,3,4}
b = {3,4,5,6}
a | b # {1, 2, 3, 4, 5, 6}
set.union(a,b) # {1, 2, 3, 4, 5, 6}
a & b # {3, 4}
set.intersection(a,b) # {3, 4}
a - b # {1, 2}
set.difference(a,b) # {1, 2}
a ^ b # {1, 2, 5, 6}
set.symmetric_difference(a,b) # {1, 2, 5, 6}
##

a = {1,2,3,4}
a |= {5}
a # {1, 2, 3, 4, 5}

a = {1,2,3,4}
a.update({5})
a # {1, 2, 3, 4, 5}

a = {1,2,3,4}
a &= {0,1,2,3,4}
a # {1, 2, 3, 4}

a = {1,2,3,4}
a.intersection_update({0,1,2,3,4})
a # {1, 2, 3, 4}

a = {1,2,3,4}
a -= {3}
a # {1, 2, 4}

a = {1,2,3,4}
a.difference_update({3})
a # {1, 2, 4}

a = {1,2,3,4}
a ^= {3,4,5,6}
a # {1, 2, 5, 6}
a = {1,2,3,4}
a.symmetric_difference_update({3,4,5,6})
a # {1, 2, 5, 6}
##

a = {1,2,3,4}

a <= {1,2,3,4} # True
a.issubset({1,2,3,4,5}) # True
a < {1,2,3,4} # False

a >= {1,2,3,4} # True
a.issuperset({1,2,3,4}) # True
a > {1,2,3} # True

a == {1,2,3,4} # True
a == {4,2,1,3} # True
a != {1,2,3} # True

a.isdisjoint({5,6,7,8}) # True
a.isdisjoint({3,4,5,6}) # False
##

a = {1,2,3,4}

a.add(5) # {1, 2, 3, 4, 5}

a.remove(3) # {1, 2, 4, 5}
a.remove(3) # KeyError: 3
a.discard(2) # {1, 4, 5}
a.discard(3) # {1, 4, 5}

a.pop() # 1, {4, 5}
a.pop() # 4, {5}

a.clear() # set()

len(a) # 0
##

a = {1,2,3,4}
b = a
a is b # True
b.add(5)
a # {1, 2, 3, 4, 5}
b # {1, 2, 3, 4, 5}

a = {1,2,3,4}
b = a.copy()
a is b # False
a == b # True
b.add(5)
a # {1, 2, 3, 4}
b # {1, 2, 3, 4, 5}
##

a = {1,2,3,4}
for i in a:
    print(i)
'''
1
2
3
4
'''
##

a = {i for i in 'apple'}
a # {'e', 'p', 'a', 'l'}

a = {i for i in 'pineapple' if i not in 'apl'} # {'n', 'i', 'e'}