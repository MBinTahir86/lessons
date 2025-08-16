sub1=float(input("enter the marks of maths:"))
sub2=float(input("enter the marks of english:"))
sub3=float(input("enter the marks of science:"))
sub4=float(input("enter the marks of sst:"))
sub5=float(input("enter the marks of computer:"))

sum=(sub1+sub2+sub3+sub4+sub5)
print(sum)
avr=(sum/5)
print(avr)
if avr >= 91 and avr <= 100:
    print("your grade is A1")
elif avr >= 81 and avr <=91:
    print ("your grade is A2")
elif avr >=71 and avr <= 81:
    print("your grade is B1")
elif avr >= 61 and avr <= 71:
    print("your grade is B2")
else:
    print(" invalid statement")