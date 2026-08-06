import turtle
# create a turtle
screen=turtle.Screen()
pen=turtle.Turtle()
# pen.color("red")
# pen.penup()
# screen.bgcolor("pink")
# pen.forward(100)
# pen.right(100)
# pen.forward(100)
# pen.color("blue")
# pen.left(100)
# pen.backward(100)


#change the background color to yellow and draw a square
screen.bgcolor("yellow")
for i in range(4):
    pen.forward(100)
    pen.right(90)
for i in range(4):
    pen.color("blue")
    pen.forward(100)
    

turtle.done()
