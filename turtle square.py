import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(800,900)
square=turtle.Turtle()
length=70
num_sides=4
angle=360/num_sides
for i in range(num_sides):
    square.forward(length)
    square.right(angle)

turtle.done()
