class Sample:
    def __init__(self,name):
        self.name=name
    def getString(self):
        self.name=input("Enter a message")
    def printString(self):
        print(self.name.upper())
s1=Sample("")
s1.getString()
s1.printString()
