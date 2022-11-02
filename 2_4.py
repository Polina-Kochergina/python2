import random
class Dice(object):
    def __init__(self, sides):
        self.sides = sides
        self.x = []
        # self.r = random.randint(1,self.sides)
        # self.history.append(self.r)

    def roll(self):
        self.r = random.randint(1,self.sides)
        self.x.append(self.r)
            # x.append(a)
        # if len(x) >= 5:
            # x.pop(0)
        return(self.x)

    def show_history(self):
        while len(self.x) > 5:
            self.x.pop(0)
        print(self.x)

        return(self.x)
        

def roller(n, m):
    cubes = []
    roll = []
    for i in range(1,n+1):
        cubes.append(Dice(m))
        print(f"{i} кубик = {cubes[i-1].roll()}")

roller(10, 6)
