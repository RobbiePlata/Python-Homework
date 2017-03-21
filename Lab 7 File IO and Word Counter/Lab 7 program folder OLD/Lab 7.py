#read from an input file, display each line of text to the screen
#write each line of text to an output file
#the user shall specify the name of the output file
#each line displayed and written shall be preceded with a line number
#at the end the program shall display and write an analysis of tbhe file
#including the following facts: minimum words in any line, max words in any line,
#, total words in input file, average number of words per line.
#program shall never abort

def file():
    go = True
    while go:
        try:
            fileName = input("What is the name of the file: ")
            readFile = open(fileName, "r")
            go = False
        except:
            print("'"+fileName+"'"+" does not exist")
    return readFile

def stripFile(file1):
    try:
        file1 = open(file, "r")
        file1 = file.strip()
        hasMultiSpaces=True
        while hasMultiSpaces:
            oldLength=len(file1)
            file1 = file.replace("  "," ")
            if (len(file) == oldLength):
                print(file1)
                hasMultiSpaces = False
    except Exception as err:
        print(err)
    return file

def count(sentence):
    wordCount = 0
    sentence = sentence.strip()
    for i in range (0, len(sentence)):
        if (sentence[i]==" "):
            wordCount += 1
    if (len(sentence)>0):
        wordCount += 1
    print("\n"," - Words in line:", wordCount)
    return wordCount

def outFile():
    userFile = input("What do you want to name the new file:")
    fileWrite = open(userFile, "w")
    userInput = input("Write to the file:")
    fileWrite.close()
    return userFile
    
#Main
try:
    file1 = file()
    for lineOfText in file1:
        stripFile = stripFile(lineOfText)
        print (lineOfText,end="")
        read = ("\n", count(lineOfText))
except Exception as error:
    print(error)
