height=float(input("write the height in centimeters"))
weight=float(input("write the weight in kg"))
bmi=weight/(height/100)**2
print("your bmi is",bmi)
if bmi <= 18.4:
    print("you are under weight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<=29.9:
    print ("over- weight")
else:
    print("obese")