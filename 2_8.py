def make_ndim_vector_class(n):
    class Vector():
            # dim = n

        def __init__(self, *args):
            if len(args) != n:
                print("размер не соотв")
                exit(0)
            else:
                self.coord = args

        def get_length(self):
            return(len(self.coord))
            
        def show(self):
            return self.coord

        def __add__(self, other):
            summ = []
            if len(self.coord) == len(other.coord):
                for idx in range(len(self.coord)):
                    summ.append(self.coord[idx] + other.coord[idx])
            else:
                print("разная размерность")
            return summ          
    return Vector
          
Vector3 = make_ndim_vector_class(3)
v1 = Vector3(1, 3, 5)
Vector2 = make_ndim_vector_class(2)
v2 = Vector3(3, 5, 0)
print(v1 + v2)



# v1 = Vector(7, -1, 5)
# v2 = Vector(2, -4, 9)
# print(v2 + v1)
# print(Vector.get_length(v1))
# print(Vector.show(v1))
# # # v2 = Vector([1, 3, 5])

# print(v1)

# def printScores(*scores):
#    print(f"Student Name: Vector")
#    for score in scores:
#     print(score)
# printScores([100, 95, 88, 92, 99])