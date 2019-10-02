class Point:

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __init__(self, x, y):  # This is class method 
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x},{self.y})")


p = Point.zero()

p.draw()