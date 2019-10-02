class Point:
    def __init__(self, x, y): #constructor __init__ is used to define constructor
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(2,3)

point.z = 20 

point.draw()


print(point.z)


another = Point(10,29)

print(f"AnotherPoint({another.x},{another.y})")


