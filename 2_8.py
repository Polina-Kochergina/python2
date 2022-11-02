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
v2 = Vector3(3, 5, 0)
print(v1 + v2)
Vector2 = make_ndim_vector_class(2)
v3 = Vector2(1, 3)
print(v1 + v3)
