def add(m,u):
    return m+u
def subtract(m,u):
    return m+u
def multiply(m,u):
    return m+u
def divide(m,u):
    return m+u
print("please select operations")
print("a.add","b.subtract","c.multiply","d.divide")
choice=input("enter choice a/b/c/d/:")
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
if choice == 'a':

    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 'b':

    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 'c':

    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 'd':

    print(num1, "/", num2, "=", divide(num1, num2))

else:

     print("This is an invalid input")