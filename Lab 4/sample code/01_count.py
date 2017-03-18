# Demonstrate While Loop by writing messages that
# display counter values as they increment.

import turtle

FAST=1 # 1 millisecond is fast
SLOW=500 # this is about 1/2 of a second (quite noticeable)

# get a reference to the turtle's screen, so we can later change the speed fast/slow
screen = turtle.Screen()

MSG_X = -150 # we will write the message on the left side (b/c x is a negative numbe)
MSG_Y = 150  # we will write the message on the top (b/c y is a positive number)
MSG_SIZE = 48 # Large font size for message

turtle.hideturtle() # do not want to see the little triangle

numTimes = 4
i=1

while i <= numTimes:
        # Only go inside this block if i is <= numTimes 

        # do not want to see a line going to this position
        turtle.penup()
        turtle.goto(MSG_X, MSG_Y) # x is negative (left side), y positive (top)

        # write the value of i then set the speed slow, so we can see it
        turtle.color("black")
        turtle.write(i,font = ("Times", MSG_SIZE, "bold", "italic"))
        screen.delay(SLOW) # Once we see the first number, slow down so we can see everything

        # do not want to see a line going to this position
        turtle.penup()
        turtle.goto(-150, 150) # x is negative (left side), y positive (top)

        # write the value of i again, in white -- to "erase" it
        turtle.color("white")
        turtle.write(i,font = ("Times", MSG_SIZE, "bold", "italic"))
        
        i=i+1
        # after i is incremented, the flow of control goes up to the while statement

turtle.done()
