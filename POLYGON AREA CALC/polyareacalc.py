# class square
class square:

    def __init__(self, side):
        self.side = side

    def area(self):
        print("My area is :", self.side**2)

# class circle
class circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("My area is :", 3.14*self.radius*self.radius)

# object creation
osquare = square(int(input("Enter the side of square : ")))
ocircle = circle(int(input("Enter the radius of circle : ")))

# iterating through objects
for shape in (osquare, ocircle):
    shape.area()