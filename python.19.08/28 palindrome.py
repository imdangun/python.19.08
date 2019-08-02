word = input('단어를 입력하세요.')

isPalindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-(1+i)]:
        isPalindrome = False
        break

print(isPalindrome)
'''
단어를 입력하세요.>? level
True
'''
'''
단어를 입력하세요.>? hello
False
'''
##

word = input('단어를 입력하세요.')
print(word == word[::-1])
'''
단어를 입력하세요.>? level
True
'''
'''
단어를 입력하세요.>? hello
False
'''
##

word = 'level'
word[::-1] # 'level'
word == word[::-1] # True

list(word) == list(reversed(word)) # True
list(word) # ['l', 'e', 'v', 'e', 'l']
list(reversed(word)) # ['l', 'e', 'v', 'e', 'l']
word == ''.join(reversed(word)) # True
##

text = 'hello'
for i in range(len(text)-1):
    print(text[i], text[i+1], sep='')
'''
he
el
ll
lo
'''
##

text = 'this is python script'
words = text.split()

for i in range(len(words)-1):
    print(words[i], words[i+1])
##

text = 'hello'
two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')
'''
he
el
ll
lo
'''
##

text = 'this is python script'
words = text.split()
list(zip(words, words[1:]))
# [('this', 'is'), ('is', 'python'), ('python', 'script')]

list(zip(['hello','ello','llo']))
# [('hello',), ('ello',), ('llo',)]
list(zip(*['hello','ello','llo']))
# [('h', 'e', 'l'), ('e', 'l', 'l'), ('l', 'l', 'o')]