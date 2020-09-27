def N(a):
    if (a<=5.7) and (a>=-2.4):
        N=a**2
    else:
        N=4
    print('значение функции = ',N)
a=float(input('Введите число : '))
N(a)
