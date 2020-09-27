def SL(a1,a2,b1,b2,c1,c2):
    d=a1*b2-a2*b1
    x=(c1*b2-c2*b1)/d
    y=(a1*c2-a2*c1)/d
    print('x= '+str(x)+' y= ',y)
print('Введите 6 коэфицентов')
a1,a2,b1,b2,c1,c2=map(int,input().split())
SL(a1,a2,b1,b2,c1,c2)
