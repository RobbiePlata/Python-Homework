def menu(prompt):
    tf = True
    print ("Enter 1 : Print")
    print ("Enter 2 : Search")
    print ("Enter 3 : Insert")
    print ("Enter 4 : Delete")
    print ("Enter 5 : Leave")
    while tf:
        try:
            userInput = input(prompt)
            if userInput == "1":
                print()
                userInput = "Print"
                tf = False
            elif userInput == "2":
                userInput = "Search"
                tf = False
            elif userInput == "3":
                userInput = "Insert"
                print()
                tf = False
            elif userInput == "4":
                userInput = "Delete"
                tf = False
            elif userInput == "5":
                userInput = "Leave"
                tf = False
            else:
                print()
            return userInput
        except Exception as error:
            (error)



def openFile(prompt, fileName):
    print()
    file = open(fileName, "r")
    print(prompt)
    print()
    return file



def printFile(teams):
    for lineOfText in teams:
        lineOfText = lineOfText.strip()
        teamNames = lineOfText[0:10]
        record = lineOfText[10:20]
        record = record.strip()
        print ("["+teamNames+"]"+format("["+record+"]",'^10s'))
    print()
    print("Printing Successful!")



def search(prompt, file):
    searchWord = input(prompt)
    for lineOfText in file:
        return search



def writeToFile(fileName):
    file = open(fileName, "a")
    return file



def clearScreen(menu):
    for i in range(0,40):
        print()




START = 0
NAME_LEN = 10
SCORE_LEN = 20
Teams = openFile("Printing File", "TeamsAndRecords.txt")
#Defining Lists
TeamNameList = []
TeamScoreList = []
program = True
while program:
    Menu = menu("Choose another option.")
    if Menu == "Print":
        clearScreen(Menu)
        Teams = openFile("Printing File", "TeamsAndRecords.txt")
        print ("NFL Team Standings")
        printText = printFile(Teams)
    elif Menu == "Search":
        clearScreen(Menu)
        Teams = openFile("Reading File", "TeamsAndRecords.txt")
        askUser = ("What are you looking for?")
        searchFile = search(askUser, Teams)
        print ()
        print()
    elif Menu == "Insert":
        newStrings = insert("What team do you want to add?", "What is their record?", "TeamsAndRecords.txt")
        clearScreen(Menu)
        print()
    elif Menu == "Delete":
        clearScreen(Menu)
        print()
    elif Menu == "Leave":
        print()
        print("G")
        print("  O")
        print("    O")
        print("      D")
        print("        B")
        print("          Y")
        print("            E")
        print()
        program = False
