ask1=float(input("enter the cost of ticket for one person :"))
ask2=float(input ("enter the number of people :"))
var=ask1*ask2
print("the total cost for ticket for",ask2,"people is :",var)
ask3=float(input("enter the cost of room of hotel per night :"))
ask4=float(input("enter the number of nights stayed in hotel :"))
ask5=float(input("enter the people stayed in hotel ;"))
var2=ask3*ask4*ask5
print("the total cost of hhotel is :",var2)
ask6=float(input("enter the cost of rent of car rent per day :"))
ask7=float(input("enter the number of days car was rented :"))
var3=ask6*ask7
print("the total cost of car rent is :",var3)

total_cost=var+var2+var3
print ("thetotal expense of trip is :",total_cost)