#sequence type: list, tuple, range, str

a = [1,2,3]
1 in a # True
6 in a # False
6 not in a # True

1 in (1,2,3) # True
1 in range(3) # True
'e' in 'hello world' #True

a = [1,2]
b = [3,4]
a + b # [1, 2, 3, 4]

range(1,3) + range(3,5) # unsupported operand type(s) for +: 'range' and 'range'
list(range(1,3)) + list(range(3,5)) # [1, 2, 3, 4]
'hello' + 'world' # 'helloworld'
'hello' + 1 # TypeError: can only concatenate str (not "int") to str
'hello' + str(1) # 'hello1'

[1,2] * 3 # [1, 2, 1, 2, 1, 2]
range(1,3) * 3 # TypeError: unsupported operand type(s) for *: 'range' and 'int'
list(range(1,3)) * 3 # [1, 2, 1, 2, 1, 2]
tuple(range(1,3)) * 3 # (1, 2, 1, 2, 1, 2)
'hello' * 3 # 'hellohellohello'

len([0,1,2]) # 3
len((0,1,2)) # 3
len(range(0,3)) #3
len('hello world') # 11

a = [10,20,30]
a[0] # 10
a[2] # 30
a[3] # IndexError: list index out of range

(10,20,30)[0] # 10
range(10,40,10)[0] # 10
'hello'[0] # 'h'
[10,20,30][-1] # 30
(10,20,30)[-1] # 30
range(10,40,10)[-1] # 30
'hello'[-1] # o
a = 'hello'
a[len(a)-1] # o


# update
a = [0, 0, 0]
a[0] = 10
a[1] = 20
a[2] = 30
a # [10, 20, 30]

a = (0, 0, 0)
a[0] = 10 #TypeError: 'tuple' object does not support item assignment
a = range(10,40,10)
a[0] = 1 # TypeError: 'range' object does not support item assignment
a = 'hello'
a[0] = 'w' # TypeError: 'str' object does not support item assignment


# del
a = [1,2,3]
del a[1]
a # [1, 3]
a = (1,2,3)
del a[1] # TypeError: 'tuple' object doesn't support item deletion
a = range(1,4)
del a[1] # TypeError: 'range' object doesn't support item deletion
a = 'hello'
del a[1] # TypeError: 'str' object doesn't support item deletion


# slice - list
a = [10,20,30,40,50]
a[0:4] # [10, 20, 30, 40]
a[1:1] # []
a[2:3] # [30]
a # [10, 20, 30, 40, 50]
a[0:5] # [10, 20, 30, 40, 50]
a[0:5:2] # [10, 30, 50]
a[:3] # [10, 20, 30]
a[1:] # [20, 30, 40, 50]
a[:]  # [10, 20, 30, 40, 50]
a[::] # [10, 20, 30, 40, 50]
a[:5:2] # [10, 30, 50]
a[0::2] # [10, 30, 50]
a[::2]  # [10, 30, 50]
a[0:len (a)] # [10, 20, 30, 40, 50]
a[:len(a)]  # [10, 20, 30, 40, 50]

# slice - tuple
a = (10,20,30,40,50)
a[1:3] # (20, 30)
a[1:]  # (20, 30, 40, 50)
a[:4:2] # (10, 30)

# slice - range
a = list(range(10,60,10))
a[1:3] # [20, 30]

# slice - str
a = 'hello world'
a[4:7] # 'o w'
a[4:]  # 'o world'
a[0::2] # 'hlowrd'

a = [0,1,2,3,4,5]
a[1:3] = ['a','b'] # [0, 'a', 'b', 3, 4, 5]
a[1:3] = ['c'] # [0, 'c', 3, 4, 5]
a[1:2] = ['s','k','y'] # [0, 's', 'k', 'y', 3, 4, 5]

del a[1:4] # [0, 3, 4, 5]
del a[0:4:2] # [3, 5]