import random


print("This is a math quiz")


totalCorrect = 0
count = 1

bad=True
while(bad):
    try:
        print()
        numOfQuestions=input("How many questions do you want? ")
        numOfQuestions=int(numOfQuestions)
        if(numOfQuestions>=1):
            bad=False
        else:
            print("Please enter a number greater than zero")
    except:
        print("Thats not a number")

for count in range(1,numOfQuestions+1):

    x= random.randint(1,9)
    y = random.randint(1,9)

    print()
    prompt = str(count) + ". How much is " + str(x) + " plus "+ str(y) + "? "
    answer = input(prompt)
    answer = int(answer) 
    
    if answer == x + y:
        print("you are right")
        totalCorrect = totalCorrect + 1 
    else:
        print("you are wrong")

print()
print("Congratulations. You got", totalCorrect, "right.")

