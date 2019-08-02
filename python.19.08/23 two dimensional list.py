a = [[1,2],[3,4],[5,6]] # [[1, 2], [3, 4], [5, 6]]
a[0][0] # 1
a[1][1] # 4
a[0][0] = 100 # [[100, 2], [3, 4], [5, 6]]

# jagged list
a = [[1,2],
     [3,4,5],
     [6,7,8,9]] # [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
from pprint import pprint
pprint(a, indent=1, width=20)

a = []
a.append([])
a[0].append(1)
a[0].append(2) # [[1, 2]]
a.append([])
a[1].append(3)
a[1].append(4)
a[1].append(5) # [[1, 2], [3, 4, 5]]

a=((1,2),(3,4)) # ((1, 2), (3, 4))
b=([1,2],[3,4]) # ([1, 2], [3, 4])
c=[(1,2),(3,4)] # [(1, 2), (3, 4)]
a[0][0] = 100 # TypeError: 'tuple' object does not support item assignment
b[0][0] = 100 # ([100, 2], [3, 4])
b[0] = [1,2] # TypeError: 'tuple' object does not support item assignment
c[0][0] = 100 # TypeError: 'tuple' object does not support item assignment
c[0] = (100,200) # [(100, 200), (3, 4)]

a = [[1,2],[3,4],[5,6]]
for x,y in a:
     print(x,y)
'''
1 2
3 4
5 6
'''

a = [[1,2],[3,4],[5,6]]
for i in a:
    for j in i:
         print(j, end=' ')
     print()
'''
1 2 
3 4 
5 6 
'''

a = [[1,2],[3,4],[5,6]]
for i in range(len(a)):
     for j in range(len(a[i])):
          print(a[i][j], end=' ')
     print()
'''
1 2 
3 4 
5 6 
'''

a = []
for i in range(10):
     a.append(i)
print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


a = []
for i in range(3):
     line = []
     for j in range(2):
          line.append(j)
     a.append(line)
print(a) # [[0, 1], [0, 1], [0, 1]]


a = [[j for j in range(2)] for i in range(3)] # [[0, 1], [0, 1], [0, 1]]
a = [[0]*2 for i in range(3)] # [[0, 0], [0, 0], [0, 0]]


a = [3,1,3,2,5]
b = []
for i in a:
     line = []
     for j in range(i):
          line.append(j)
     b.append(line)
print(b) # [[0, 1, 2], [0], [0, 1, 2], [0, 1], [0, 1, 2, 3, 4]]


students = [
     ['john','C',19],
     ['maria','A',25],
     ['andrew','B',7]
]
a = sorted(students, key=lambda student: student[0])
# [['andrew', 'B', 7], ['john', 'C', 19], ['maria', 'A', 25]]
a = sorted(students, key=lambda student: student[1])
# [['maria', 'A', 25], ['andrew', 'B', 7], ['john', 'C', 19]]

students = [
     ['최한석','C',19],
     ['김보라','A',25],
     ['양승일','B',7]
]
a = sorted(students, key=lambda student: student[0])
# [['김보라', 'A', 25], ['양승일', 'B', 7], ['최한석', 'C', 19]]

# copy, deepcopy
a = [1,2]
b = a
a[0] = 100
print(b) # [100, 2]

import copy
a = [1,2]
c = copy.deepcopy(a)
a[0] = 100
print(c) # [1, 2]