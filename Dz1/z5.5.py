def N(k,t):
    if k=='343':
      S=t*15
      print('Стоимость звонка в Екатерибург '+str(S)+' руб.')
    elif k=='381':
        S=t*18
        print('Стоимость звонка в Омск '+str(S)+' руб.')
    elif k=='473':
        S=t*13
        print('Стоимость звонка в Воронеж '+str(S)+' руб.')
    elif k=='485' :
        S=t*11
        print('Стоимость звонка в Ярославль '+str(S)+' руб.')
    else:
        print('Неправильно введен код региона')
k=input('Введите код города : ')
t=int(input('Введите длительность разговора в минутах : '))
N(k,t)
