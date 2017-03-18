# Demonstrate using a sprite

import turtle

# Define speed constants 
SPEED=50 # 250 milliseconds is 1/4 of a second, 500 is half a second

# Define constants related to size of screen
MAX_X=360
MAX_Y=200
turtle.setup(2*MAX_X, 2*MAX_Y) # specify size of window
turtle.bgpic("flowerBg3.gif") # and background image

turtle.penup()
turtle.hideturtle()
turtle.goto(-100,-100)

turtle.addshape("horse.gif")
turtle.shape("horse.gif")
turtle.showturtle()

turtle.done()
