# Demonstrate While Loop Using a circle that changes (color/size) a
# certain number of times (numTimes, value has been set to 4)

import turtle
import random

FAST=5 # 5 milliseconds is fast
SLOW=1000 # this is about 1/2 of a second (quite noticeable)

# get a reference to the turtle's screen, so that later we can
# change the display speed fast/slow
screen = turtle.Screen()

turtle.hideturtle()
turtle.shape("circle")

numTimes = 4
i=1

while i <= numTimes:
        # Only go inside this block if i is <= numTimes 

        # hide the turtle then quickly change its size and color
        screen.delay(FAST)
        turtle.hideturtle()
        turtle.color("yellow", "blue") # color of border, color of shape
        turtle.shapesize(4,4,8) # x stretch, y stretch, border size

        # circle is ready. Show it, then slow down the display and
        # show it again. 
        turtle.showturtle()
        screen.delay(SLOW) 
        turtle.showturtle()
         
        # hide the turtle then quickly change it to a second size and color
        screen.delay(FAST)
        turtle.hideturtle()
        turtle.color("green", "purple")
        turtle.shapesize(8,8,24)

        # circle is ready again (different size/color). Show it, then slow down
        # and show it again.
        turtle.showturtle()
        screen.delay(SLOW)
        turtle.showturtle()
        
        i=i+1
        # after i is incremented, the flow of control goes up to the while statement

turtle.done()
