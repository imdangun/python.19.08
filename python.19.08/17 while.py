cnt = 1
while cnt > 0:
    cnt = int(input())
    print(cnt)
# >? 2
# 2
# >? 3
# 3
# >? 0
# 0


import random
random.random() # 0.6611156898463783
random.randint(1,6) # 3

i = 0
while i != 3:
    i = random.randint(1,6)
    print(i)
# 6
# 3

dice = [1,2,3,4,5,6]
random.choice(dice) # 6

while True:
    i = random.randint(1,10)
    print(i)
    if(i==3): break
# 10
# 2
# 1
# 2
# 3
