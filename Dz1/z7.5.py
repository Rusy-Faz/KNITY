import doctest

def f (x):
    q = x**4 + 4**x
    return q
  

x = int(input('Введите число: '))
print (doctest.testmod(f(x)))
