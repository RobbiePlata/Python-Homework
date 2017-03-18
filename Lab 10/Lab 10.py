# Sally Kyvernitis
# Robert Cyril Plata III
# 11/17/2015
# Array of Turtles Lab 10
# I made this accuracy tester themed by my favorite 1998 game.
# Mutalisks are flying zerg units in the game Starcraft.
# Try to aim as well as possible. The less shots you take and the more kills you get..
# The better your accuracy gets. The more kills you get the harder it will become to shoot the mutalisks.
# Good luck
# The program will end at 30 kills.





import turtle # import turtle object
import random # import turtle object
screen = turtle.Screen() # screen variable now controls turtle screen
explosion = [] # explosion list
muta = [] # muta list
MAX_X = 1280 # resolution of the picture to fit window height
MAX_Y = 720 # resolution of the picture to fit window width
clickCount = 0 # clickCount is the amount of times you click
kill = 0 # kill is the amount of kills you have currently. Every kill will be in shell.
TITLE = "Shoot the flying units on scren. Be as accurate as possible." # Constant to write
NAME = "Robbie Plata" # Constant to write
screen.delay(5) # speed for screen

for i in range(0, 47): # for loop to append to a list
    explosion.append("Explosion "+str(i)+".gif") # 46 Explosion i.gif pics.

for i in range(0, 5): # for loop to append mutalisk movement to list muta
    muta.append("muta "+str(i)+".gif") # append muta i.gif to muta

for i in range(0, len(explosion)):# for loop the length of explosion list
    turtle.addshape(explosion[i]) # add shapes to use for future turtles

for i in range(0, len(muta)):# for loop the length of muta list
    turtle.addshape(muta[i]) # add shapes to use for future turtles

def explosionFunc(x, y): #x and y are for the x and y axis of the mouse click
    global kill # without global, you will get an error for undefined variables.
    global countLocation # Same as above. Using the global variable.
    kill += 1 # kill = an explosion
    explode.showturtle() # show the explosion
    for i in range(0, 47): #for the range of the pics 0-46
        explode.penup() # lift pen as not to show the line
        explode.goto(x, y) # go to the mouse click x and y
        explode.pendown() # pen down to show explosion
        explode.shape(explosion[i]) # explode pic which will be ran through the loop 
        explode.penup()# pen up so the next click doesnt make a line
    if kill == 5: # Some messages for the user wherever their mouse cursor clicked last.
        turtle.write("Is this too easy for you? Lets speed this up.", font = ("Terminal", 12, "bold", "normal")) # signaling to the user that it will speed up
    if kill == 10: # Messages for the user wherever their mouse cursor clicked last.
        turtle.write("Impressive.", font = ("Terminal", 12, "bold", "normal"))
    if kill == 20: # Messages for the user wherever their mouse cursor clicked last.
        turtle.write("INSANE", font = ("Terminal", 12, "bold", "normal"))
    turtle.color("red") # color red for a kill
    turtle.goto(x,y) # go to the mouse cursor
    turtle.write(kill, font = ("Terminal", 12, "bold", "normal")) #write kill count
    print("Kills:",kill) # print kill count in shell
    
def calcRatio(num1, num2): # num1 is kill, num2 is clickCount 
    if num2 == 0: # if num2 is 0, do not divide because you cannot divide by zero.
        ratio = 1 # ratio = 1 instead 
        return ratio # return the ratio
    ratio = num1/num2 # divide kill by clickCount for accuracy sake
    return ratio # return the ratio

def clicks(x, y): # click location x y
        turtle.color("White") # color for turtle
        global clickCount # global variable called in function
        turtle.penup() #pen up for no line drag
        turtle.goto(x,y) # go to the mouse click
        clickCount += 1 #clickCount is increased
        if clickCount == 50: # if the clickCount is 50 then tell the user they are bad at aiming.
            turtle.write("50 shots. Does your finger hurt yet?", font = ("Terminal", 12, "bold", "normal"))
        if clickCount == 100: # if clickCount reaches 100 then make fun of the user more
            turtle.write("You are still going? lol", font = ("Terminal", 12, "bold", "normal"))
        print (clickCount,"shots") # print clickcount in shell
        print("Shot Accuracy:", calcRatio(kill,clickCount)) # print shot accuracy calling the func

#series of print messages for the start of the program.
print("Use your mouse to chase this little guy down.")
print("Try to be as accurate as possible.")
print("The more kills you get, the harder it will get.")
print("Kills are shown on the screen as well as in the shell.")

turtle.penup() # penup to eliminate lines


turtle.setup(MAX_X,MAX_Y) # size for the window
turtle.bgpic("background.gif") # background picture
turtle.color("White") # turtle color for writing name and title.
turtle.goto(-MAX_X/3,MAX_Y/2.25) # go to this location for writing title
turtle.write(TITLE, font = ("Terminal", 18, "bold", "normal"))
turtle.goto(MAX_X/7,-MAX_Y/4) # go to this location for writing name 
turtle.write(NAME, font = ("Terminal", 18, "bold", "normal"))
mutalisk = turtle.Turtle() # defining mutalisk
mutalisk2 = turtle.Turtle()# defining mutalisk2
mutalisk3 = turtle.Turtle()# defining mutalisk3
mutalisk4 = turtle.Turtle()# defining mutalisk4
explode = turtle.Turtle() # define explode
explode.hideturtle() # explode hideturtle 
mutalisk.penup() # pen up for elimination of drag
mutalisk2.penup()# pen up for elimination of drag
mutalisk3.penup()# pen up for elimination of drag
mutalisk4.penup()# pen up for elimination of drag
accuracy = calcRatio(kill, clickCount)
while kill < 30 : # while the kill count is less than 30 run the program.
    if kill > 1: # whole speed is 5 when greater than 1 
        screen.delay(4) 
    elif kill >= 5: # whole speed is 3 when greater than or = to 5
        screen.delay(3)
    elif kill >= 10: # whole speed is 2 when greater than or equal to 10
        screen.delay(2)
    elif kill >= 20: # whole speed is 1 when greater than or equal to 20
        screen.delay(1)
    for i in range(0, 5): # for i in range of pic 0 to pic 4 because of the number of sprite pics
        xMuta = random.randint(-MAX_X/2,MAX_Y/2) #x axis for muta 1
        yMuta = random.randint(-MAX_X/2,MAX_Y/2) #y axis for muta 1
        xMuta2 = random.randint(-MAX_X/2,MAX_Y/2) #x axis for muta 2
        yMuta2 = random.randint(-MAX_X/2,MAX_Y/2) #y axis for muta 2
        xMuta3 = random.randint(-MAX_X/2,MAX_Y/2) #x axis for muta 3
        yMuta3 = random.randint(-MAX_X/2,MAX_Y/2) #y axis for muta 3
        xMuta4 = random.randint(-MAX_X/2,MAX_Y/2) #x axis for muta 4
        yMuta4 = random.randint(-MAX_X/2,MAX_Y/2) #y axis for muta 4
        mutalisk2.goto(xMuta2, yMuta2) # tell the sprite to go to x and y randomly
        mutalisk2.shape(muta[i]) # the shape of the object for visual
        mutalisk2.onclick(explosionFunc) # When clicking on the object, explode.
        mutalisk.goto(xMuta, yMuta)
        mutalisk.shape(muta[i]) # the shape of the object for visual
        mutalisk.onclick(explosionFunc) # When clicking on the object, explode.
        mutalisk3.goto(xMuta3, yMuta3)
        mutalisk3.shape(muta[i]) # the shape of the object for visual
        mutalisk3.onclick(explosionFunc) # When clicking on the object, explode.
        mutalisk4.goto(xMuta4, yMuta4)
        mutalisk4.shape(muta[i]) # the shape of the object for visual
        mutalisk4.onclick(explosionFunc) # When clicking on the object, explode.
        screen.onclick(clicks) # what allows me to click is this <<<<
turtle.color("Red") # color red for turtle
turtle.write("Well done. Check your accuracy in Shell.", font = ("Terminal", 12, "bold", "normal")) # Write that the program has ended.
print("================================") # border seperation 
print("Accuracy =", accuracy,"Shots =", clickCount, "Kills =", kill) # Accuracy shots and kills analysis
print()
print()
turtle.done() # finished. Stop program
