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

def searchFun(presName):
    # For each line of text in the input file
    # write that line of text to the screen
    for lineOfText in fileHandler:
        strippedLine = lineOfText.strip()
        if (presName == strippedLine):
            print ("==>  match ==>", end="")
        print(lineOfText,end="") # Note: end="" just means not to print a newline afterwards (else it will double space)

def delete(presName):
    # For each line of text in the input file
    # write that line of text to the screen
    for lineOfText in fileHandler:
        strippedLine = lineOfText.strip()
        if (presName != strippedLine):
            print(lineOfText,end="")

def insert(presName):
    # For each line of text in the input file
    # write that line of text to the screen
    inserted=False
    for lineOfText in fileHandler:
        strippedLine = lineOfText.strip()
        if (strippedLine > presName):
            if (not inserted):
                print (presName)
            inserted=True
        #else:
            #print ("line of text not greater than", presName)
        print()
        print(lineOfText,end="")

# main

fileHandler=getInputFile()
searchPresName= input("Enter the name of a president: ")
insert(searchPresName)
fileHandler.close()

