
inputFile=open("phoneNums.txt","r")
for lineText in inputFile:
	
	# remove the carriage return that's at the end of the line that you just read
	lineText=lineText[0:len(lineText)-1] 

	name=lineText[0:30]
	number=lineText[30:55]
	print ("["+name+"] ["+number+"]")
print (lineText)
