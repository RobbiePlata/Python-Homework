import random

# bottom up example -- working on a single user interaction first.
# So it is not inside of the main loop.
# We are pretending that this is question number 3...

x = random.randint(1,9)
y = random.randint(1,9)
questionNum=3
bad=True
while (bad):
    print()
    questionType=input("Question "+str(questionNum)+". Enter A=addition, S=subtraction: ")
    questionType=questionType.strip()
    questionType=questionType.upper()
    #print ("questionType",questionType) # this was here for debug purposes
    if questionType=="A":
        bad=False
        prompt = "==> How much is " + str(x) + " plus "+ str(y) + "? "
        answer = input(prompt)
        answer = int(answer) # Note: we have not yet validated this input
        if answer == x + y:
            print("you are right")
            totalCorrect = totalCorrect + 1 
        else:
            print("Sorry, that is not the right answer.")
    elif questionType=="S":
        bad=False
        prompt = "==> How much is " + str(x) + " minus "+ str(y) + "?"
        answer = input(prompt) # Note: we have not yet validated this input
        answer = int(answer)
        if answer == x - y:
            print("you are right")
            totalCorrect = totalCorrect + 1 
        else:
            print("Sorry, that is not the right answer.")
    else:
        print("That is not a valid choice.")
       
