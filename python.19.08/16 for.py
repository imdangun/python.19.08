for i in range(10):
    print(i, 'hello')
# 0 hello
# 1 hello
# 2 hello
# 3 hello
# 4 hello
# 5 hello
# 6 hello
# 7 hello
# 8 hello
# 9 hello

for i in range(0,10,2):
    print(i, 'hello')
# 0 hello
# 2 hello
# 4 hello
# 6 hello
# 8 hello

for i in range(10,0,-1):
    print(i, 'hello')
# 10 hello
# 9 hello
# 8 hello
# 7 hello
# 6 hello
# 5 hello
# 4 hello
# 3 hello
# 2 hello
# 1 hello

for i in reversed(range(10)):
    print(i, 'hello')
# 9 hello
# 8 hello
# 7 hello
# 6 hello
# 5 hello
# 4 hello
# 3 hello
# 2 hello
# 1 hello
# 0 hello

cnt = int(input('반복 횟수'))
for i in range(cnt):
    print(i, 'hello')
# 반복 횟수>? 10
# 0 hello
# 1 hello
# 2 hello
# 3 hello
# 4 hello
# 5 hello
# 6 hello
# 7 hello
# 8 hello
# 9 hello

a = [1,2,3]
for i in a:
    print(i)
# 1
# 2
# 3

fruits = ('사과','딸기','포도')
for fruit in fruits:
    print(fruit)
# 사과
# 딸기
# 포도

for letter in 'python':
    print(letter)
# p
# y
# t
# h
# o
# n

for letter in reversed('python'):
    print(letter)
# n
# o
# h
# t
# y
# p

for i in range(5):
    for j in range(5):
        print('j:', j, end=' ')
    print(' i: ', i)
'''
j: 0 j: 1 j: 2 j: 3 j: 4  i:  0
j: 0 j: 1 j: 2 j: 3 j: 4  i:  1
j: 0 j: 1 j: 2 j: 3 j: 4  i:  2
j: 0 j: 1 j: 2 j: 3 j: 4  i:  3
j: 0 j: 1 j: 2 j: 3 j: 4  i:  4
'''

for i in range(5):
    for j in range(5):
        print('*', end='')
    print()
'''
*****
*****
*****
*****
*****
'''

for i in range(5):
    for j in range(5):
        if j<=i:
            print('*', end='')
    print()
'''
*
**
***
****
*****
'''