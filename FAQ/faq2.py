mas=[i for i in range(10)]
mas.append(5)

mas.sort()
for i in range(len(mas)-1):
    if mas[i]==mas[i+1]:
        print(mas[i])
