from random import*
x1 = randint(1,6)
x2 = randint(1,6)
if x1 > x2 :
    print ('Победил первый игрок ')
elif x1 < x2:
    print ('Победил второй игрок ')
else:
    print ('Ничья ')
