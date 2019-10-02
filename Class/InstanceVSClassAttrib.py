class Point:
    color = "red"  # This is the class variable

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(1, 2)

print(point.color)

another = Point(10, 29)
print(another.color)
