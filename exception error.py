try:
    var=int(input("enter a number"))
    print(var)
except ValueError as a:
    print(a)

print("this is out of exception")