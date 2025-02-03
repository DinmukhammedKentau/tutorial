class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self):
        self.length = int(input("Enter the length of the rectangle"))
        self.width = int(input("Enter the width of the rectangle"))
    def area(self):
        print(self.length * self.width)
r1=Rectangle()
r1.area()