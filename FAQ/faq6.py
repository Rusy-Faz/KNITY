a=[1,2,3,3,4,5,3,6]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(a)
print(b)
