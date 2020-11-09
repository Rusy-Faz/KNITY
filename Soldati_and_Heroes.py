from random import randint
class Soldat:
    count = 0   #идентификатор

    def __init__(self, c):
        self.id = Soldat.count
        Soldat.count += 1
        self.command = c

class Hero(Soldat):
    def __init__(self, c):
        Soldat.__init__(self, c)
        self.level = 1

    def up_level(self):
        self.level += 1

class Soldat2(Soldat):
    def __init__(self, c):
        Soldat.__init__(self, c)
        self.my_hero = None

    def follow(self, hero):
        print("Солдат под номером ", self.id, " следует за героем ", hero.id)

h1 = Hero(1)
h2 = Hero(2)

ves1 = []
ves2 = []

for i in range(20):
    n = randint(1, 2)
    if n == 1:
        ves1.append(Soldat2(n))
    else:
        ves2.append(Soldat2(n))

print("У", h1.id, "героя", len(ves1), "солдат" 
      "\nУ", h2.id, "героя", len(ves2), "солдат")

print("Уровни", len(ves1), len(ves2))
if len(ves1) > len(ves2):
    h1.up_level()
    ves1[0].follow(h1)
elif len(ves1) < len(ves2):
    h2.up_level()
    ves1[0].follow(h2)
