def addEntry(name,number):
	friendName.append(name)
	friendNumber.append(number)
	
def printInfo():
	print()
	
	# recall that this line prints the value of x (as a string) in 15 spaces
	#  format (x, "15s") 
	print (format("Name",NAME_FORMAT), format("Number",PHONE_FORMAT))
	
	# print some dashes just for looks
	for i in range (0,NAME_LEN+PHONE_LEN):
		print ("-", end="")
	print()
	
	# now print the actual values from the parallel arrays
	for i in range(0,len(friendName)):
		print (format(friendName[i],NAME_FORMAT), format(friendNumber[i],PHONE_FORMAT))
		
# MAIN PROGRAM
		
# Tells python you want to have an array named "friendName'
# and another array named "friendNumber".
friendName=[]
friendNumber=[]

# It is important to use the same values for these lengths everywhere (when reading, 
# when formatting, when writing), so use NAMED_CONSTANTS.
NAME_LEN=30
PHONE_LEN=20

# use these formats for column headings as well as values in the columns (so everything lines up)
NAME_FORMAT=str(NAME_LEN)+"s"
PHONE_FORMAT=str(PHONE_LEN)+"s"

# add some "hard coded" data into the parallel arrays
addEntry("Able, Arthur", "215 897-1334")
addEntry("Farkus, Fred", "215 597-1354")
addEntry("Jones, Joe", "610 789-1456")
addEntry("Smith, Sally", "215 987-1445")
addEntry("Thomas, Terry", "610 497-5634")
addEntry("Wiggins, Walt", "610 867-1389")
 
# print the parallel arrays before the delete
printInfo()

i=2 # suppose we want to delete the entry in position 2 (Jones, Joe -- remember it all starts with position 0)
friendName.pop(i)
friendNumber.pop(i)

# print the parallel arrays after the delete
printInfo()
