import math
class Point:
    def __init__(self):
        print("Enter initial x1 y1  \n")
        x1,y1=map(int,input().split())
        self.x1=x1
        self.x2=0
        self.y1=y1
        self.y2=0
    def show(self):
        print(self.x1,self.y1)


    def move(self):
        print("Enter point to move x2 y2\n")
        x2,y2 = map(int,input().split())
        self.x2=x2
        self.y2=y2
    def dist(self):
        d=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        print(d)

p1=Point()
p1.show()
p1.move()
p1.dist()