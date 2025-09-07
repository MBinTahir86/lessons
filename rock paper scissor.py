import random

var1=str(random.choice(['rock','paper','scissor']))
var2=input("enter your choice : rock/paper/scissor :")
if var1==var2:
    print("its a tie")
elif (var1=='rock' and var2=='scissor') or (var1=='paper' and var2=='rock') or (var1=='scissor' and var2=='paper'):
    print("you lost")
    print("the computer chosed",var1)