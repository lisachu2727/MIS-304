#Tzu-Chuan Chu

#Importing modules
import turtle
import my_graphics

#Variables for square
xSquare = -100
ySquare = -100
widthSquare = 200
colorSquare = 'pink'

#Variables for circle
xCircle = 0
yCircle = 0
radiusCircle = 75
colorCircle = 'light green'

#Variables for text in the circle
text = 'Welcome to the \n Cake Program'
font = ('Arial', 16, 'normal')

#Defining main function
def main():
    #Hiding turtle cursor
    turtle.hideturtle()

    #Creating square background
    my_graphics.square(xSquare, ySquare, widthSquare, colorSquare)

    #Creating circle
    my_graphics.circle(xCircle, yCircle, radiusCircle, colorCircle)

    #Writing text in circle
    my_graphics.write(text, font)

#Calling main function
main()
