a = [1,2,3]
a.append(4) # [1, 2, 3, 4]
len(a) # 4

a = [1,2,3]
a.append([4,5]) # [1, 2, 3, [4, 5]]
len(a) # 4

a = [1,2,3]
a.extend([4,5]) # [1, 2, 3, 4, 5]
len(a) # 5

a = [1,2,3]
a.insert(2,100) # [1, 2, 100, 3]
len(a) # 4
a.insert(len(a),200) # [1, 2, 100, 3, 200]
a.insert(4,[4,5]) # [1, 2, 100, 3, [4, 5], 200]
a[5:1] = [6,7] # [1, 2, 100, 3, [4, 5], 6, 7, 200]

a = [1,2,3]
a.pop() # [1, 2]
a.pop(0) # [2]
a.pop(0) # []
a.extend([1,2,3]) # [1, 2, 3]
del a[1] # [1, 3]
a.remove(1) # [3]
a.extend([2,3]) # [3, 2, 3]
a.remove(3) # [2, 3]

a = [1,2,2,2,3]
a.index(2) # 1
a.count(2) # 3

a = [1,2,3]
a.reverse() # [3, 2, 1]

a = [5,2,3,1,4]
a.sort() # [1, 2, 3, 4, 5]
a[-1] # 5
a.clear() # []
a.extend([1,2]) # [1, 2]
del a[:] # []

a = [1,2,3]
b = a
a is b # True
a[2] = 5
b[2] # 5
c = a.copy()
a[2] = 6
b[2] # 6
c[2] # 5
a is c # False

for i in [1,2,3]:
    print(i)
'''
1
2
3
'''

a = [1,2,3]
for idx, val in enumerate(a):
    print(idx,': ',val)
'''
0 :  1
1 :  2
2 :  3
'''

a = [1,2,3]
for idx, val in enumerate(a, start=2):
    print(idx,': ',val)
'''
2 :  1
3 :  2
4 :  3
'''

a = [1,2,3]
for i in range(len(a)):
    print(a[i])
'''
1
2
3
'''

# list comprehension
a = [i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = list(i for i in range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [i+5 for i in range(10)] # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
a = [i*2 for i in range(10)] # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

a = [i for i in range(10) if i%2==0] # [0, 2, 4, 6, 8]
a = [i+2 for i in range(10) if i%2==0] # [2, 4, 6, 8, 10]
a = [i*j for i in range(2,10) for j in range(1,10)] # [2,4,...,72,81]

a = [1.1, 2.2, 3.3]
a = list(map(int ,a)) # [1, 2, 3]
a = list(map(str, range(5))) # ['0', '1', '2', '3', '4']

# >? 1 2 를 입력하면
a = input() # '1 2'
a = input().split() # ['1', '2']
a = list(map(int, input().split())) # [1, 2]

a, b = [1,2] # a=1, b=2
x = input().split() # ['1', '2']
m = map(int, x) # <map object at 0x02E691F0>
a, b = m # # a=1, b=2

a = [1,2,3]
min(a) # 1
max(a) # 3
sum(a) # 6


# tuple
a = (1,2,3,2)
a.index(2) # 1
a.count(2) # 2

a = (1,2,3)
for i in a:
    print(i, end=' ')
'''
1 2 3 
'''

# tuple comprehension
a = tuple(i for i in range(10) if i%2==0) # (0, 2, 4, 6, 8)
(i for i in range(10) if i%2==0) # <generator object <genexpr> at 0x02E603B0

a = (1.1,2.2,3.3)
a = tuple(map(int,a)) # (1, 2, 3)

a = (1,2,3)
min(a) # 1
max(a) # 3
sum(a) # 6