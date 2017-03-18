def makeRevealedWord(guess,key,revealedWord):
    newWord= ""
    for j in range (0,len(key)):
        if (guess == key[j:j+1]):
            print ("Correct.")
            newWord = newWord+guess
        else:
            newWord =newWord + revealedWord[j:j+1]
        print ("Revealed word is", newWord)
    return  newWord

def makeInitialRevealedWord(key):
    revealedWord = ""
    for i in range (0,len(key)):
        revealedWord += "*"
    print("Revealed word is", revealedWord)
    return revealedWord

def countStars(word):
    countStars=0
    for i in range(0,len(word)):
        if word[i:i+1]=="*":
            countStars=countStars+1
    return countStars
#main
secretKey = "TEMPLE" 

showWord = makeInitialRevealedWord(secretKey)
print ("showWord is",showWord)

letterGuess = input ("Please enter a letter: ")
letterGuess = letterGuess.upper()
print ("You entered ", letterGuess)

showWord= makeRevealedWord (letterGuess,secretKey,showWord)
print ("new showWord is",showWord)


print("The number of stars is" ,countStars(showWord))
