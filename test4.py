# class Parent1:
#     def __init__(self, parent1):
#         self.parent1 = parent1
#
#     def show_p1(self):
#         return self.parent1
#
#
# class Parent2:
#     def __init__(self, parent2):
#         self.parent2 = parent2
#
#     def show_p2(self):
#         return self.parent2
#
#
# class Child(Parent1, Parent2):
#     def __init__(self, parent1, parent2):
#         self.parent1 = parent1
#         self.parent2 = parent2
#
#     def show(self):
#         print("I am child")
#         print(self.parent1)
#         print(self.parent2)
#
# child1 = Child("P1", "P2")
# child1.show()


class vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def details(self):
        print("I am Vehicle")
        print("Mileage of vehicle is :", self.mileage)
        print("Cost of vehicle is :", self.cost)


class color():
    def __init__(self, carcolor):
        self.carcolor = carcolor
    def detail(self):
        print("Color of vehicle is:", self.carcolor)


class car(vehicle, color):
    def __init__(self, milage, cost, carcolor):
        vehicle.__init__(self,milage,cost)
        color.__init__(self,carcolor)
    def show_car(self):
        print("I am car")

c = car(200, 400, "red")
print(c.carcolor)
print(c.cost)
print(c.mileage)

# c = car.__init__(vehicle,200, 400)
# c = car(vehicle.__init__(400, 4000, 500), color.__init__('hee'))












