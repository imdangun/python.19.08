file = open('hello.txt','w')
file.write('hello world')
file.close()
##

with open('hello.txt','r') as file:
    s = file.read()
    print(s)
# hello world
##

with open('hello.txt','w') as file:
    for i in range(3):
        file.write('hello world {0}\n'.format(i))
##

lines = ['안녕\n', '널\n', '본다.']
with open('hello.txt','w') as file:
    file.writelines(lines)
##

with open('hello.txt','r') as file:
    lines = file.readlines()
    print(lines)
# ['안녕\n', '널\n', '본다.']

with open('hello.txt','r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))
'''
안녕
널
본다.
'''
##

file = open('hello.txt','r')
a, b, c = file
a, b, c # ('안녕\n', '널\n', '본다.')
##

import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'kor':90, 'eng':95, 'math':100}

with open('james.pic','wb') as file:
    pickle.dump(name,file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

with open('james.pic','rb') as file:
    name2 = pickle.load(file)
    age2 = pickle.load(file)
    address2 = pickle.load(file)
    scores2 = pickle.load(file)

print(name2)
print(age2)
print(address2)
print(scores2)
'''
james
17
서울시 서초구 반포동
{'kor': 90, 'eng': 95, 'math': 100}
'''