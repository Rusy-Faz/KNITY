def find_pars(L,summ):
    s = set(L)
    edgeCase = summ/2
    if L.count(edgeCase) ==2:
        print (edgeCase, edgeCase)
    s.remove(edgeCase)      
    for i in s:
        diff = summ-i
        if diff in s: 
            print (i, diff)

L = [1,2,3,11,7,9,5,8]
summ = 10          
find_pars(L,summ)
