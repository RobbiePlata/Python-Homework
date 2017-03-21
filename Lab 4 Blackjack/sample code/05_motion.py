# Demonstrate While Loop by making a circle that change color and size a
# certain number of times (numTimes, value has been set to 4)

import turtle

# Define speed constants 
SPEED=50 # 250 is 1/4 of a second, 500 is 1/2 a second

#Define constants related to size of screen
MAX_X=360
MAX_Y=200
turtle.setup(2*MAX_X, 2*MAX_Y) # specify size of window
turtle.bgpic("flowerBg3.gif") # and background image

# specify initial position of turtle, lower left quadrant
x = -350
y = -100

# distance to change in the x axis and the y axis for each iteration
dX=8
dY=2

# get a reference to the turtle's screen, so that later we can
# change the display speed fast/slow
screen = turtle.Screen()

turtle.hideturtle()
turtle.penup() # do not want any tail?
turtle.shape("circle")

# "slowest" makes smooth movement between each position of the turtle
turtle.speed("slowest")

numTimes = 40
i=1

while i <= numTimes:
        # Only go inside this block if i is <= numTimes 

        # change x and y coordinates by a fixed amount
        x = x + dX
        y = y + dY
        turtle.goto(x,y)
        
        turtle.color("blue", "white") # color of border, then color of shape
        turtle.shapesize(2,2,1) # y stretch, x stretch, then border size

        # Once we see the first circle, slow down so we can see everything
        turtle.showturtle()
        screen.delay(SPEED)
        
        x = x + dX
        y = y + dY
        turtle.goto(x,y)

        turtle.color("green","white") # color of border, then color of shape
        turtle.shapesize(2,2.2,1) # y stretch, x stretch, then border size
        
        i=i+1
        # after i is incremented, the flow of control goes up to the while statement

turtle.done()
