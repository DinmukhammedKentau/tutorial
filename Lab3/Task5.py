class Account:
    def __init__(self):
        self.owner=input("Please enter your name")
        self.balance=int(input("Please enter your balance"))
        self.pin = int(input("Parol zhaz\n"))


    def deposit(self):
        print(self.balance)
    def withdraw(self,drawBalance):
        pinCode=int(input("Please enter your pincode"))
        if self.pin==pinCode:
          if(self.balance-drawBalance>=0):
            self.balance-=drawBalance
          else:print("Недостаточно средств!!!")
        else : print("Parol qate zhazdyn")
print("Hello,can you enter some info about you?")
a1=Account()
while(True):
    print("[1] get total Balance")
    print("[2] withdraw")
    print("[0] exit")
    choice=int(input())
    if choice==0:
        break
    elif choice==1:
      a1.deposit()
    elif choice==2:
        print("Please enter a withdraw")
        snyatie=int(input())
        a1.withdraw(snyatie)

