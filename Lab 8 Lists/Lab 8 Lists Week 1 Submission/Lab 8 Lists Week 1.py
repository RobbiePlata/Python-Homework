# Robert Cyril Plata III
# Sally Kyvernitis
# 10/29/2015
# Does everything but insert because Week 1 requirements
# This Prints the txt file, it can print the list version
# It can search teams, and search scores I capitalized the first letter of Team Names
# So I made this program is case sensitive.
# "Eagles" not "eagles"
# It can also delete. And it can do it over and over again.


# This is my UI
def menu(prompt):  # prompt is below in the function
    running = True  # loop so that way user enters a valid option
    print("Enter 1 : Print (text file)")
    print("Enter 2 : Search")
    print("Enter 3 : Insert")
    print("Enter 4 : Delete")
    print("Enter 5 : PrintList (List)")
    print("Enter 6 : Leave")
    while running:  # Will run until turned False
        userInput = input(prompt)
        if userInput == "1":
            print()
            userInput = "Print"
            running = False  # Turned False here and below when proper option is chosen.
        elif userInput == "2":
            userInput = "Search"
            running = False
        elif userInput == "3":
            userInput = "Insert"
            print()
            running = False
        elif userInput == "4":
            userInput = "Delete"
            running = False
        elif userInput =="5":
            userInput = "PrintList"
            running = False
        elif userInput == "6":
            userInput = "Leave"
            running = False
        else:
            print()
            print("Sorry,", userInput, "is not an option.")
            print()
        return userInput


# Function opens the file
def openFile(fileName):
    file = open(fileName, "r")  # Reads the file
    return file  # Returns the file if needed elsewhere

# Prints List so that way the user can see what the list looks like
def printList():
    print()
    order = 0
    for m in range(0,len(teamName)): # prints each line neatly until completion
        print(format(teamName[m], NAME_FORMAT), "  ", format(teamWins[m], WIN_FORMAT).strip(),"   ",format(teamLoss[m], LOSS_FORMAT).strip(),"   ",("["+str(order)+"]").strip())
        order += 1
    print()
    print("Team /", "Wins /", "Losses /", "index")
    print()

# Prints straight from the text file if the user wants to see what they started with
def printFile(teams):
    for lineOfText in teams:  # Prints each line neatly until completion
        lineOfText = lineOfText.strip()
        teamNames = lineOfText[START:NAME_LEN]
        record = lineOfText[NAME_LEN:LOSS_LEN]
        record = record.strip()
        print(teamNames+format(""+record, '^10s'))
    print()
    print("Printing Successful!")

def searchList(searchName):  # Searches the list and returns the parallel equal
    for i in range (0, len(teamName)):
        if teamName[i].startswith(searchName):
            return i  # Returns number
    return -1  # Returns -1 so the rest wont run in Main

# writeToFile (not used yet.)
def writeToFile(fileName):
    file = open(fileName, "a")
    return file

# Make the screen free of last prompt
def clearScreen(menu):
    for i in range(0, 40):
        print()

# Deletes a string in the list
def deleteItem(deleteElement):
    for i in range(deleteElement, len(teamName)-1):
        teamName[i] = teamName[i+1]
    teamName.pop()

# Constants
START = 0
NAME_LEN = 9
WIN_LEN = 18
LOSS_LEN = 22
NAME_FORMAT = str(NAME_LEN)+"s"
WIN_FORMAT = str(WIN_LEN)+"s"
LOSS_FORMAT = str(LOSS_LEN)+"s"

# Defining Lists
Teams = openFile("TeamsAndRecords.txt")
teamName = []  # List defining
teamWins = []  # List defining
teamLoss = []  # List defining

# Defining arrays
for lineOfText in Teams:
    name = lineOfText[START:NAME_LEN]  # length that i want an array
    name = name.strip()  # removing unnecessary spaces
    teamName.append(name)  # Add line to list teamName until completion
    wins = lineOfText[NAME_LEN:WIN_LEN]  # length i want the second array
    wins = wins.strip()  # removing unnecessary spaces
    teamWins.append(wins)  # Add line to list teamWins until completion
    loss = lineOfText[WIN_LEN:LOSS_LEN]  # length wanted for third array
    loss = loss.strip()  # removing unnecessary spaces
    teamLoss.append(loss)  # Add line to list teamLoss until completion

ON = True
while ON:
    Menu = menu("Choose an option.")  # prompt

    # Print function
    if Menu == "Print":
        clearScreen(Menu)  # Clear screen function initiate
        Teams = openFile("TeamsAndRecords.txt")  # Open File
        print(format("   Football Teams"),)  # Title
        print()
        print("Teams    Wins  Losses")  # Labels
        print("------------------------")  # Border
        printFile(Teams)  # Initiate printFile function

    # Search Function
    elif Menu == "Search":
        askSearch = input("What are you looking for?")
        index = searchList(askSearch)  # users input is searched
        if index >= 0:  # If the user enters a number less than zero throw exception
            print()
            print("Found:", teamName[index], "with a record of", teamWins[index], "and", teamLoss[index])
            print()
        else:
            print()
            print(askSearch, "not found (Remember: This program is case sensitive!)")
            print()

    # Insert Function
    elif Menu == "Insert":
        Teams = openFile("TeamsAndRecords.txt")
        print("Work in progress")
        print()

    # Delete Function
    elif Menu == "Delete":
        element = input("What team do you want to remove?")
        searchDelete = searchList(element)
        if element in teamName:
            deleteItem(searchDelete)
            print(element, "deleted")  # Prints the user's new list
            print()
        else:
            print()
            print(element, "Not in list")
            print()

    # Simple PrintList option
    elif Menu == "PrintList":
        printList()
            
    elif Menu == "Leave":  # User chooses leave
        print()
        print("Final list is:")
        printList()
        print()
        print("G")
        print("  O")
        print("    O")
        print("      D")
        print("        B")
        print("          Y")
        print("            E")
        print("              !!")
        ON = False  # ON is now False program is off.

