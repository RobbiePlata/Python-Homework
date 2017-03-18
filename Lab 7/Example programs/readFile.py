def getInputFile ():
    go = True
    while go:
        try:
            fileName = input ("Enter file name: ")
            # Open file for input
            myfile = open(fileName, "r") # Note: "r" means open for reading.
            go = False
        except:
            print ("bad file name")
    return myfile

# main
fileHandler=getInputFile()

# For each line of text in the input file
# write that line of text to the screen
for lineOfText in fileHandler:
    print(lineOfText,end="") # Note: end="" just means not to print a newline afterwards (else it will double space)

fileHandler.close()
