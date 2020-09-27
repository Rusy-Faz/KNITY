def N(a,b):
    if a>b:
       print('Наибольшее число = ',a)
    elif b>a:
        print('Наибольшее число = ',b)
    else:
      print('Числа равны')  
a=float(input('Введите первое число : '))
b=float(input('Введите второе число : '))
N(a,b)
