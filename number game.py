import random
play =True
var1=str (random.randint(10,20))
while play:
    guess=input("enter you guess between 10 and 20")
    if guess==var1:
        print("you won")
        print("the number is",var1)
        
    else:
        print("wrong guess")
        print("the number was",var1)



