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
        

 
# d1 = Dice(18)
# d2 = Dice(18)
# print(d1.sides, d2.sides)
# for idx in range(0,12):
#     d1.roll()
#     d2.roll()
#     # print(d1.show_history())
#     # print(d2.show_history())
# d2.roll()
# d1.roll()
# print(d1.show_history())
# print(d2.show_history())


def roller(n, m):
    cubes = []
    roll = []
    for i in range(1,n+1):
        cubes.append(Dice(m))
        print(f"{i} кубик = {cubes[i-1].roll()}")

roller(10, 10)



# print(d2.sides)
# for idx in range(0,12):
#     d2.roll()
# print(d2.show_history())
# d2.roll()
# print(d2.show_history())



# def roller(n):
#     d = [0]*n
#     for idx in range(0,n):
#         d[idx] = Dice(10)
#         print(d[idx].roll())
#         print(d[idx].show_history())
#     # print(d)
# roller(10)

# n = 5
# m =6

# for i in range(n):
#     l =[]
#     for j in range(m):
#         l.append(random.randint(1, 100))
#     print(l)