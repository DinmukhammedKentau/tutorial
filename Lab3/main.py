class  Student:
    def __init__(self):
        print("Creating new object")
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getSgtring(self):
        print("Hello World")
s1=Student("Almas",18)
print(s1.name,s1.age)
s1.age=20
print(s1.name,s1.age)
s1.getSgtring()

