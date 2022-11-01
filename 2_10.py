def square(x):
    return x**2


class FunctionCache(object):

    def __init__(self, fun):
        self.y = fun
        self.cach = []
        self.arg = []
        # print("Instance Created")


    def __call__(self, x):

        if x in self.arg:
            idx = self.arg.index(x)
            f = self.cach[idx]
            print(f"Repeated call for x = {x}")
            
        else:
            f = self.y(x)
            self.cach.append(f)
            self.arg.append(x)
            print(f"First time call for x = {x}")

        return f

sq_cach = FunctionCache(square)

print(sq_cach(2))
print(sq_cach(5))
print(sq_cach(5))
print(sq_cach(5))
print(sq_cach(7))


print(sq_cach.cach)
