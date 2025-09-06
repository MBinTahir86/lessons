try:
    num1=int(input("enter a number:"))
    num2=int(input("enter the second number:"))
    result=num1/num2
    print("the result is",result)
except ZeroDivisionError:
    print("you cannot divide a number by zero")
except ValueError:
    print("please enter a numeric value")
except NameError as ex :
    print(ex)
except:
    print("same error occured")
finally:
    print("i will execute")