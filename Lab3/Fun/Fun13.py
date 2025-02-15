import random
def guessTheNumber():
    c=1
    print("Hello! What is your name?")
    name=input()
    print("Well,"+name+",I am thinking of a number between 1 and 20.")
    b=random.randint(1,20)
    a = int(input())
    while True:
        if a!=b:
            if a>b:
                print("Your guess is too high\nTake a guess.")
            elif a<b:
                print("Your guess is too low\nTake a guess.")
            c+=1
            a=int(input())

        else:
            print("Good job,"+name+",you guessed my number in "+str(c)+"guesses")
            break
guessTheNumber()

