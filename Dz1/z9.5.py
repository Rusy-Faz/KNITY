from random import*

a =  ['самовар', 'весна', 'лето']
b = choice(a) #слово
c = choice(b) #буква
d = list(b) #буквы из слова
e = b.index(c)
d[e] = '?'
f = ''.join(d)     
print(f)

j = input('Введите букву: ')
if j == c:
    print('Победа!')
else:
    print('Попробуйте еще раз :( ')
