I = [3, 'Hello', 7, 4, 'Привет', 4, 3, -1]

if 'Привет' in I:
    I.remove('Привет')
    print(I)
if I.count(4) > 1:
    I.clear()
    print(I)
