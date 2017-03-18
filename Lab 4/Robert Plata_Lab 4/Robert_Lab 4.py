#Sally Kyvernitis
#9/20/2015
#blackjack game using loops
import random
print(format("Welcome to blackjack", '^75s')) # centered

print()
#all variables
stand=0
wins=0
loss=0
tries=0
count=1
value=random.randint(1,11)
everything = stand + wins + loss
tf=True
#while true, how many tries, if tries greater than or = to 1, then false.
while(tf):
    try:
        tries=input("How many tries do you want? ")
        tries=int(tries)
        if tries >= 1:
            tf=False
        else:
            print("Enter a number")
    except:
        print()
        print("Enter a number, not letters.")
        print()
#try block containting while loop.
try:        
    while value < 21 and everything != tries: #while the value is under 21 and everything isnt equal to tries.
        print ()
        print ("Value is",value)
        print ()
        askuser=input("Hit me? Yes or No ")
        askuser=askuser.upper()
        askuser=askuser.strip()
        #yes will promt a hit
        if askuser == "YES":
            value = value + random.randint(1,11)
            if value > 21:
                print(value,"is over 21. You lose.")
                loss = loss + 1
                print()
                print("You have won", wins," games, lost", loss, "times and stood", stand,"times.")
                value=0
                everything = everything + 1
                print(everything)
                count=count+1
            #value equal to 21 will equal a win.
            if value == 21:
                wins = wins + 1
                print()
                print (value, "You win!")
                print("You have won", wins," games, lost", loss, "times and stood", stand,"times.")
                value=0
                everything = everything + 1
                count=count+1
        #no will stop a hit. And add a stand.
        if askuser == "NO":
            stand=stand+1
            print ("You stopped at", value)
            value = 21
            print()
            print("You have won", wins," games, lost", loss, "games and stood", stand,"times.")
            value=0
            everything = everything + 1
            count=count+1
        #everything equaling tries will end the program
        if everything == tries:
            print()
            print("You tried " + str(tries) + " times!")
#this will print error message and tell user to type a number.
except Exception as error:
    print("You need to type a number.")
    tf=False
    print(error)
