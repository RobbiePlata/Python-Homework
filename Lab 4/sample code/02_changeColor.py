# Demonstrate While Loop by making a circle that change color and size a
# certain number of times (numTimes, value has been set to 4)

import turtle

SLOW=500 # this is about 1/2 of a second (quite noticeable)

# get a reference to the turtle's screen, so that later we can
# change the display speed fast/slow
screen = turtle.Screen()

turtle.shape("circle")

numTimes = 4
i=1

while i <= numTimes:
        # Only go inside this block if i is <= numTimes 

        turtle.color("yellow", "blue") # color of border, then color of shape
        turtle.shapesize(4,4,8) # x stretch, y stretch, then border size

        # Once we see the first circle, slow down so we can see everything
        screen.delay(SLOW) 

        turtle.color("green", "purple") # color of border, then color of shape
        turtle.shapesize(8,8,24) # x stretch, y stretch, then border size
        
        i=i+1
        # after i is incremented, the flow of control goes up to the while statement

turtle.done()
