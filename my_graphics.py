#Tzu-Chuan Chu

#Importing turtle
import turtle

#Defining square function
def square(x, y, width, color):
    turtle.penup()
    #Starting at lower left corner
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    #Loop for turtle to turn
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

#Defining circle function
def circle(x, y, radius, color):
    turtle.penup()
    #Starting in the middle of circle
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

#Defining write function
def write(text, font):
    turtle.penup()
    #Location of text
    turtle.goto(-72, -25)
    #Taking in variables for text
    turtle.write(text, font=font)
