class A:
    def __init__(self, x,m):
        self.x = x
        self.m = m
        print("Initializing A with x =", x)

class B:
    def __init__(self, y):
        self.y = y
        print("Initializing B with y =", y)

class C(A, B):
    def __init__(self, x, y,m, z):
        print("Initializing C with z =", z)
        A.__init__(self,x,m)
        B.__init__(self,y)
        self.z = z

c = C(1, 2, 3,4)