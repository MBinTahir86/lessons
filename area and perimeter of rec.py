def area(length,breadth):
    return length*breadth
def perimeter(length,breadth):
    return 2*(length+breadth)
    lentgh=int(input("enter the lentgh"))
    breadth=int(input("enter the breadth"))
    print ("area is", area(length,breadth))
    print ("perimeter is", perimeter(length,breadth))
    



def area(length, breadth):
    return length * breadth

def perimeter(length, breadth):
    return 2 * (length + breadth)

length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

print("Area of the rectangle is", area(length, breadth))
print("The perimeter of the rectangle is", perimeter(length, breadth))