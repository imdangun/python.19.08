def plus(x):
    return x+10

plus(1) # 11
##

lambda x:x+10 # anonymous function

plus = lambda x:x+10
plus(2) # 12

(lambda x:x+10)(3) # 13

y=10
(lambda x: x+y)(4) # 14
##

def plus(x):
    return x+10

list(map(plus, [1,2,3])) # [11, 12, 13]

list(map(lambda x:x+10, [1,2,3])) # [11, 12, 13]
##

(lambda: 1)() # 1

x=10
(lambda: x)() # 10
##

a=[1,2,3,4,5,6,7,8,9,10]
list(map(lambda x: str(x) if x%3==0 else x, a))
# [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

list(map(lambda x: str(x) if x==1 else float(x) if x==2 else x+10, a))
# ['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]

def trans(x):
    if x==1:
        return str(x)
    elif x==2:
        return float(x)
    else:
        return x+10

list(map(trans, a)) # ['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]
##

a = [1,2,3,4,5]
b = [2,4,6,8,10]
list(map(lambda x,y:x*y, a, b)) # [2, 8, 18, 32, 50]
##

def nums(x):
    return x>5 and x<10

a = [8,3,2,10,15,7,1,9,0,11]
list(filter(nums,a)) # [8, 7, 9]

list(filter(lambda x:x>5 and x<10, a)) # [8, 7, 9]

[i for i in a if i>5 and i<10] # [8, 7, 9]