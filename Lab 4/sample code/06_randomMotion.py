# Demonstrate While Loop by making a circle that change color and size a
# certain number of times (numTimes, value has been set to 4)

import turtle
import random

# Define speed constants 
SPEED=50 # 250 milliseconds is 1/4 of a second, 500 is half a second

# Define constants related to size of screen
MAX_X=360
MAX_Y=200
turtle.setup(2*MAX_X, 2*MAX_Y) # specify size of window
turtle.bgpic("flowerBg3.gif") # and background image

# get a reference to the turtle's screen, so that later we can
# change the display speed fast/slow
screen = turtle.Screen()

turtle.shape("circle")
turtle.penup() # do not want a line to the initial position
turtle.hideturtle() # do not want a black circle to go to the initial position

# "slowest" makes smooth movement between each position of the turtle
turtle.speed("slowest")

# specify initial position of turtle, lower left quadrant
x = -360
y = -100

numTimes = 50
i=1

while i <= numTimes:
        # Only go inside this block if i is <= numTimes 

        # change x and y a little bit with some randomness
        x = x + random.randint(2,4)
        y = y + random.randint(-2,3)
        turtle.goto(x,y)
        turtle.color("blue", "white") # color of border, then color of shape
        turtle.shapesize(1,1,1) # y stretch, x stretch, then border size
        turtle.showturtle()

        # Once we see the first circle, slow down so we can see everything
        screen.delay(SPEED) 

        x = x + random.randint(2,4)
        y = y + random.randint(1,5)
        turtle.goto(x,y)
        turtle.color("green","white") # color of border, then color of shape
        turtle.shapesize(1,1.2,1) # y stretch, x stretch, then border size
        
        i=i+1
        # after i is incremented, the flow of control goes up to the while statement

turtle.done()
