def getInputFile ():
    go = True
    while go:
        try:
            #fileName = input ("Enter file name: ")
            fileName="pres.txt"
            # Open file for input
            myfile = open(fileName, "r") # Note: "r" means open for reading.
            go = False
        except:
            print ("bad file name")
    return myfile

def search(presName):
    # For each line of text in the input file
    # write that line of text to the screen
    for lineOfText in fileHandler:
        strippedLine = lineOfText.strip()
        if (presName == strippedLine):
            print ("==>  match ==>", end="")
            
       # Note: end="" just means not to print a newline afterwards (else it will double space)
        print(lineOfText,end="") # lineOfText already has a newline in it.
 
def delete(presName):
    # For each line of text in the input file
    # write that line of text to the screen
    for lineOfText in fileHandler:
        strippedLine = lineOfText.strip()
        if (presName != strippedLine):
            print(lineOfText,end="")

# write the president name at the end of the file.
def append(presName):
    # For each line of text in the input file
    # write that line of text to the screen
    for lineOfText in fileHandler:
        print(lineOfText,end="")
    print (presName)

# write the president name at the end of the file,
# but only if the president name is not alreayd in the file.
def appendNoDups(presName):
    # For each line of text in the input file
    # write that line of text to the screen
    found=False
    for lineOfText in fileHandler:
        strippedLine = lineOfText.strip()
        if presName == strippedLine:
            found = True
        print(lineOfText,end="")
    if not found:
        print (presName)

def insertInOrder(presName):
    # For each line of text in the input file
    # write that line of text to the screen
    inserted=False
    strippedLine = "" # this is for the case of empty input file. 
    for lineOfText in fileHandler:
        strippedLine = lineOfText.strip()
        if (strippedLine > presName):
            if (not inserted):
                print (presName)
            inserted=True
        print(lineOfText,end="")

    # if the president name is "greater than" the last president
    # just append it onto the end (no insert before)
    if (presName > strippedLine):
        print (presName)

# main
fileHandler=getInputFile()
thePresName= input("Enter the name of a president: ")
choice=input("Enter A=Append, N=Append No Dups, I=Insert In Order: ")
if (choice == "A"):
    append(thePresName)
elif (choice == "N"):
    appendNoDups(thePresName)
elif (choice == "I"):
    insertInOrder(thePresName)
fileHandler.close()

