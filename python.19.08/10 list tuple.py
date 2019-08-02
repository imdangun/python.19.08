# list: 값을 변경할 수 있다.
a = [1, 2, 3, 4, 5]
person = ['최한석', 17, 180, True]

a = []
a = list()
a = list(range(10))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = list(range(0,10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = list(range(5,10)) # [5, 6, 7, 8, 9]
a = list(range(-4, 10, 2)) # [-4, -2, 0, 2, 4, 6, 8]
a = list(range(10, 0, -1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# tuple: 값을 변경할 수 없다.
a = (1, 2, 3, 4, 5)
a = 1, 2, 3, 4, 5 # (1, 2, 3, 4, 5)
person = ('최한석', 17, 180, True)
a = 1    # 1
a = (1,) # (1,)
a = 1,   # (1,)
a = tuple(range(10))        # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
a = tuple(range(5,10))      # (5, 6, 7, 8, 9)
a = tuple(range(-4, 10, 2)) # (-4, -2, 0, 2, 4, 6, 8)
a = tuple(range(10, 0, -1)) # (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

a = [1, 2, 3]
a = tuple(a)
a = (1, 2, 3)
a = list(a)

a = list('hello')  # ['h', 'e', 'l', 'l', 'o']
a = tuple('hello') # ('h', 'e', 'l', 'l', 'o')

a, b, c = [1, 2, 3] # list upacking
a # 1
b # 2
c # 3
a, b, c = (1, 2, 3) # tuple unpacking
a # 1
b # 2
c # 3

a = input().split() # >? hello world
a # ['hello', 'world']
a, b = input().split() # >? hello world
a # 'hello'
b # 'world'

