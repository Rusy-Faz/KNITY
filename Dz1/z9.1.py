I = [3, 6, 7, 4, -5, 4, 3, -1]

if sum(I) > 2 :
    print ('число элементов списка: ',len(I))

minus = max(I) - min(I)
if minus > 10 :
    print (sorted(I))
else:
    print ('Разность меньше 10')
