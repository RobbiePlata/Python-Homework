def addEntry(name,number):
	friendName.append(name)
	friendNumber.append(number)

def writeOutput():
    outfile = open("PhoneOut.txt", "w")
    nameFormat = str(NAME_KEY_LEN)+"s"
    phoneFormat = str(PHONE_LEN)+"s"
    for i in range(0,len(friendName)):
            line = format(friendName[i], nameFormat) + format(friendNumber[i], phoneFormat)
            print (line)
            outfile.write(line+"\n")
    outfile.close()

NAME_KEY_LEN=30
PHONE_LEN=20

friendName=[]
friendNumber=[]

addEntry("Smith, Sally", "215 987-1445")
addEntry("Jones, Joe", "610 789-1456")
addEntry("Able, Arthur", "215 897-1334")
 
writeOutput()
