med_cond=input("enter your medical condition: y/n")
attend=int (input("enter your attendance:"))
if (med_cond=="y"):
    print("you can attend the class")
else:
    if (attend>= 75):
        print("you can write the exam")
    else:
        print("you cannot write the exam")



