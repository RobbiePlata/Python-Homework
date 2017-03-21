#Robert C. Plata III Lab 1 8/25/2015
#This program is of a spaceship orbiting the sun.
#It isn't moving because the sun is so far away!
#The Image was resized to 600 by 600 pixels.
#fixed all lab requirements fixed
#3rd submit

import turtle  # bring in code that lets you draw things
turtle.bgpic("sun.gif")   # specify the name of your background image
turtle.resizemode("user")  # if you want to let the user to resize the screen
turtle.hideturtle()

#Ask_User
turtle.penup()
turtle.goto(0, 250)
myColor=input("What color do you want? ")
turtle.color(myColor)
myTitle=input("What title do you want? ")
turtle.write(myTitle,  font = ("Times", 16, "bold", "normal"))

#Turtle_Setting
turtle.hideturtle()
turtle.pensize (5) # make a thick line
turtle.speed("slow") # so you can see it better

#Picture_Frame

pictureWIDTH = 300
pictureHEIGHT = 300

turtle.color("red")
turtle.penup()
turtle.goto (-300, 300) # goes to the left top (assuming a 400x400 size screen)
turtle.pendown()
turtle.goto (pictureWIDTH, pictureHEIGHT) # goes to the right bottom (assuming a 400x400 size screen)
turtle.goto (pictureWIDTH, -pictureHEIGHT)
turtle.goto (-pictureWIDTH, -pictureHEIGHT)
turtle.goto (-pictureWIDTH, pictureHEIGHT)

#Spaceship_Nose
radius=51
turtle.penup()
turtle.goto(-100, -51)
turtle.fillcolor("#525152")
turtle.begin_fill()
turtle.circle(radius,-180) # move 180 degrees to left along edge of circle
turtle.end_fill()
turtle.circle(radius,180) # get back to bottom middle position of circle
turtle.pendown()

#Spaceship_Body
turtle.penup()
turtle.color("#525152")
turtle.goto(50, 50)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-100, 50)
turtle.goto(-100, -50)
turtle.goto(50, -50)
turtle.goto(50, 50)
turtle.end_fill()
turtle.pendown()

#Propulsion_Yellow
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.color("Yellow")
turtle.begin_fill() # Begin to fill color in a shape
turtle.goto(50, -50)
turtle.goto(150, 0)
turtle.goto(50, 50)
turtle.end_fill() # Fill the shape

#Propulsion_Red
turtle.penup()
turtle.goto(50, 40)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.goto(50, -40)
turtle.goto(125, 0)
turtle.goto(50, 40)
turtle.end_fill()
turtle.pendown()

#Propulsion_white
turtle.penup()
turtle.goto(50, 20)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.goto(50, -20)
turtle.goto(100, 0)
turtle.goto(50, 20)
turtle.end_fill()
turtle.pendown()

#Robbie Plata Name Bottom Right
turtle.penup()
turtle.goto(175, -275)
turtle.pendown()
turtle.color("white")
turtle.write("Robert Plata",  font = ("Times", 14, "bold", "normal") )
turtle.penup()

#Finished
turtle.done()

