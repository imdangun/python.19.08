x = 10

if x == 10:
    print('10')

if x == 10: print('10')

if x == 10:
    pass

if x == 10:
    print('10')
    print('십')

x = 15

if x>=10:
    print('10 이상')
    if x == 15:
        print('15 입니다.')
    if x == 20:
        print('20 입니다.')
# 10 이상
# 15 입니다.

x = 5
if x == 10:
    print('10입니다.')
else:
    print('10이 아닙니다.')

# False: None, False, 0, 0.0, '', "", [], (), {}, set()

if x>0 and x<20:
    print('20미만 수입니다.')
# 20미만 수입니다.
if 0<x<20:
    print('20미만 수입니다.')
# 20이하 입니다.

x = 30
if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')
else:
    print('10이나 20이 아닙니다.')
# 10이나 20이 아닙니다.

button = int(input())
if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('버튼을 잘못 눌렀습니다.')
# >? 2
# 사이다