x=int(input('숫자 입력: '))
y = 10/x
print(y)
'''
숫자 입력: >? 2
5.0
'''
'''
숫자 입력: >? 0
Traceback (most recent call last):
  File "<input>", line 2, in <module>
ZeroDivisionError: division by zero
'''
##

try:
    x = int(input('숫자 입력: '))
    y = 10 / x
    print(y)
except:
    print('예외 발생.')
'''
숫자 입력: >? 2
5.0
'''
'''
숫자 입력: >? 0
예외 발생.
'''
##

y = [10,20,30]

try:
    idx, x = map(int, input('인덱스와 숫자 입력: ').split())
    print(y[idx]/x)
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print('없는 인덱스입니다.')
'''
인덱스와 숫자 입력: >? 1 2
10.0
'''
'''
인덱스와 숫자 입력: >? 1 0
0으로 나눌 수 없습니다.
'''
'''
인덱스와 숫자 입력: >? 3 2
없는 인덱스입니다.
'''
##

y = [10,20,30]

try:
    idx, x = map(int, input('인덱스와 숫자 입력: ').split())
    print(y[idx]/x)
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.', e)
except IndexError as e:
    print('없는 인덱스입니다.', e)
'''
인덱스와 숫자 입력: >? 1 2
10.0
'''
'''
인덱스와 숫자 입력: >? 1 0
0으로 나눌 수 없습니다. division by zero
'''
'''
인덱스와 숫자 입력: >? 3 2
없는 인덱스입니다. list index out of range
'''
##

try:
    y = 10/int(input('숫자 입력: '))
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
else:
    print(y)
'''
숫자 입력: >? 2
5.0
'''
'''
숫자 입력: >? 0
0으로 나눌 수 없습니다.
'''
##

try:
    y = 10/int(input('숫자 입력: '))
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
else:
    print(y)
finally:
    print('실행을 마칩니다.')
'''
숫자 입력: >? 2
5.0
실행을 마칩니다.
'''
'''
숫자 입력: >? 0
0으로 나눌 수 없습니다.
실행을 마칩니다.
'''
##

try:
    x = int(input('숫자 입력: '))
    if x%3 != 0:
        raise Exception('3의 배수가 아닙니다.')
    print(x)
except Exception as e:
    print(e)
'''
숫자 입력: >? 3
3
'''
'''
숫자 입력: >? 2
3의 배수가 아닙니다.
'''
##

def three():
    try:
        x=int(input('숫자 입력: '))
        if x%3 != 0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    except Exception as e:
        print('A', e)
        raise

try:
    three()
except Exception as e:
    print('B', e)
'''
숫자 입력: >? 2
A 3의 배수가 아닙니다.
B 3의 배수가 아닙니다.
'''
##

def three():
    x=int(input('숫자 입력: '))
    if x%3 != 0:
        raise Exception('3의 배수가 아닙니다.')
    print(x)

try:
    three()
except Exception as e:
    print('B', e)
'''
숫자 입력: >? 2
B 3의 배수가 아닙니다.
'''
##

class NoThreeError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')

def three():
    try:
        x=int(input('3의 배수를 입력하세요.: '))
        if x%3 != 0:
            raise NoThreeError
        print(x)
    except Exception as e:
        print(e)

three()
'''
3의 배수를 입력하세요.: >? 3
3
'''
'''
3의 배수를 입력하세요.: >? 2
3의 배수가 아닙니다.
'''
##

class NoThreeError(Exception):
    pass

def three():
    try:
        x=int(input('3의 배수를 입력하세요.: '))
        if x%3 != 0:
            raise NoThreeError('3의 배수가 아닙니다..')
        print(x)
    except Exception as e:
        print(e)

three()
'''
3의 배수를 입력하세요.: >? 2
3의 배수가 아닙니다..
'''

