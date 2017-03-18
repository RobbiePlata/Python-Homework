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

turtle.shape("green0.gif")

turtle.done()
