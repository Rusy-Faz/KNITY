def ST(N):
    while N>3600:
      N=N-3600
      min=N//60
    print('Количество полных минут - ',min)
print('Введите секунды')
N=int(input())
ST(N)
