a = 'hello world'
b = a.replace('world', 'python')
print(a) # hello world
print(b) # hello python
''''''

table = str.maketrans('aeiou','12345')
a = 'apple'
b = a.translate(table)
print(a) # apple
print(b) # 1ppl2
''''''

a = 'apple pear grape'
b = a.split()
print(a) # 'apple pear grape'
print(b) # ['apple', 'pear', 'grape']

a = 'apple, pear, grape'
b = a.split(', ')
print(a) # 'apple, pear, grape'
print(b) # ['apple', 'pear', 'grape']
''''''

a = ' '
b = a.join(['apple','pear','grape'])
print(a) # ' '
print(b) # 'apple pear grape'
'-'.join(['apple','pear','grape']) # 'apple-pear-grape'
''''''

a = 'python'
b = a.upper()
c = 'PYTHON'
d = c.lower()
print(a) # python
print(b) # PYTHON
print(c) # PYTHON
print(d) # python
''''''

a = '   hello world  '
a.lstrip() # 'hello world  '
a.rstrip() # '   hello world'
a.strip()  # 'hello world'

a = ', python.'
a.strip(',.') # ' python'

import string
', python.'.strip(string.punctuation) # ' python'
string.punctuation # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
', python.'.strip(string.punctuation+' ') # 'python'
', python.'.strip(string.punctuation).strip() # 'python'
''''''

a = 'python'
a.ljust(10) # 'python    '
a.rjust(10) # '    python'
a.center(10) # '  python  '
a.rjust(10).upper() # '    PYTHON', method chaining
''''''

'3.5'.zfill(4) # '03.5'
'hello'.zfill(10) # '00000hello'
''''''

a = 'apple pineapple'
a.find('pl') # 2
a.find('xy') # -1

a.rfind('pl') # 12
a.rfind('xy') # -1
''''''

a = 'apple pineapple'
a.index('pl') # 2
a.rindex('pl') # 12
''''''

a.count('pl') # 2
''''''

'I am %s.'%'james' # 'I am james.'

name = 'maria'
'I am %10s.' % name # 'I am      maria.'
'I am %-10s.' % name # 'I am maria     .'

'%d살입니다.' % 20 # '20살입니다.'
'%.2f' % 3.145192 # '3.15'
'%5.2f' % 3.145192 # ' 3.15'

'%s %d월 5일입니다.' % ('오늘은',5) # '오늘은 5월 5일입니다.'
''''''

'Hello, {0} {2} {1}'.format('Python','Script',3.6)
# 'Hello, Python 3.6 Script'
'{0} {0} {1} {1}'.format('Python','Script')
# 'Python Python Script Script'
'Hello, {} {} {}'.format('Python','Script',3.6)
# 'Hello, Python Script 3.6'
'Hello, {language} {version}'.format(language='Python',version=3.6)
# 'Hello, Python 3.6'

language = 'Python'
version = 3.6
f'Hello, {language} {version}'
# 'Hello, Python 3.6'

'{{ {0} }}'.format('Python') # '{ Python }'

'{0:<10}'.format('python') # 'python    '
'{:<10}'.format('python')  # 'python    '
'{0:>10}'.format('python') # '    python'
'{:>10}'.format('python')  # '    python'

'%03d' % 1 # '001'
'{0:03d}'.format(35) # '035'
'%08.2f' % 3.6 # '00003.60'
'{0:08.2f}'.format(150.37) # '00150.37'

'{0:0<10}'.format(15) # '1500000000'
'{0:0>10}'.format(15) # '0000000015'
'{0:0>10.2f}'.format(15) # '0000015.00'
'{0:>10}'.format(15) # '        15'
'{0:x>10}'.format(15) # 'xxxxxxxx15'
format(1234567,',') # '1,234,567'
'%10s' % format(1234567,',') # ' 1,234,567'
'{0:,}'.format(1234567) # '1,234,567'
'{0:>10,}'.format(1234567) # ' 1,234,567'
'{0:0>10,}'.format(1234567) # '01,234,567'