x=[8,1,8,2,7,3,8,4,5,7,7]
povt=[item for item in set(x) if x.count(item)>1]
print(povt)
