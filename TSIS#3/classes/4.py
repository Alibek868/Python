import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

point1 = Point(2, 3)
point2 = Point(5, 7)


point1.show()


point1.move(4, 6)
point1.show()  


distance = point1.dist(point2)
print(f"Distance between points: {distance}")  
