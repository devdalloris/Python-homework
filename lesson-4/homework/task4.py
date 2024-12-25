import random
x=random.randint(1,100)
list1=['Y', 'YES', 'y', 'yes', 'ok']
def FindNumber():
    for i in range(10):
        k=int(input("Enter number: "))
        if k>x:
            print("Too high!")
        elif k<x:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
FindNumber()
j=input("Do you want to start again:")
if(j in list1):
    FindNumber()
else:
    print("Game is ended")

