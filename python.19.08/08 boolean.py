a, b = True, False
a, b # (True, False)

10 == 10 # True
10 != 5 #True
'python'=='python' #True
'Python'=='python' #False
'Python'!='python' #True

3 > 1 # True
3 < 1 # False
3 >= 1 # True
3 <= 1 # False

1 == 1.0 # True, == 는 값을 비교한다.
1 is 1.0 # False, is 는 메모리 주소를 비교한다.
1 is not 1.0 # True
id(1) #1839555680, 주소는 실행시마다 다르다.
id(1.0) #52113744

True and True # True
True and False # False
False and False # False

True or True   # True
True or False  # True
False or True  # True
False or False # False

not True  # False
not False # True

bool(1)       # True
bool(False)   # False
bool('False') # True