key = "TEMPLE" 
numLetters = len(key)
for i in range (0,numLetters):
    print (key[i:i+1]) 

print ("The number of letters is ", numLetters)
revealedWord = ""
for i in range (0,numLetters):
    revealedWord += "*"
print("Revealed word is", revealedWord)
    

finished = False 
while (finished == False):
    guess = input ("Please enter a letter.")
    guess = guess.upper()
    print ("You entered ", guess)

    numCorrect = 0 
    for j in range (0,numLetters):
        
        newWord = ""
        if (guess == key[j:j+1]):
            print ("Correct.")
            numCorrect += 1
            newWord = newWord+guess
        else:
            newWord =newWord + "*" #revealedWord[j:j+1]
        print ("Revealed word is", newWord)
        revealedWord = newWord
        
    print ("The number of correct letters is ", numCorrect) 

    
    finished = True 
