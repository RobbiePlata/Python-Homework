import random

totalCorrect = 0
#count = 1
#while count <= 5:
for count in range (1, 5):
    x= random.randint(1,9)
    y = random.randint(1,9)
    prompt = str(count) + ". How much is " + str(x) + " plus "+ str(y) + "? "
    
    answer = input(prompt)
    answer = int(answer)
    if answer == x + y:
        print("you are right")
        totalCorrect = totalCorrect + 1 
    else:
        print("you are wrong")
    #count = count + 1
print("The total you got right was", totalCorrect)

