# Menu Choice Loop, with clearing screen and Exit functionality

def getChoice():
        clearScreen()
        print ("1=Print")
        print ("2=Search")
        print ("3=Insert")
        print ("4=Delete")
        print ("5=Quit")
        choice = input ("What would you like to do? ")
        return choice

def clearScreen():
        for i in range (0,40):
                print ()
        # sorry, but this is the best I could do after googling a while.
        # there seems to be no way to clear the python idle shell window.

               
# Main
userChoice=getChoice()
while userChoice != "5": # but you should create NAMED-CONSTANT, don't use "5"
        
        print()
        print("Interact with user depending on what they choose")
        print()

        userChoice=getChoice()

print ("Goodbye")
