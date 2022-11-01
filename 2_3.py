class planet(object):
    def __init__(self, name, a):
        self.name = name
        self.a = a
        self.T = 365*a**(3/2)
    

    def show(self):
        print(f"Планета {self.name}. Период обращения вокруг Солнца = {self.T:.2f} суток. Большая полуось {self.a:.2f}")


pl1 = planet('Earth', 1)
pl2 = planet('Pluton', 39.48)

def hohman(planet1, planet2):
    # print(planet2.a)
    T = 3.14/86400*((1.5*(planet1.a + planet2.a)/2)**3*(10**13)/1.32712440042)**(1/2)
    return(T)


t = hohman(pl1, pl2)
print(f"время полета {pl1.name} - {pl2.name} = {t:.2f} суток")