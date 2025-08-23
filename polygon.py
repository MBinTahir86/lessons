import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(800,900)
polygon=turtle.Turtle()
length=70
num_sides=9

angle=360/num_sides
for i in range(num_sides):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()
