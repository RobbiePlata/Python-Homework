# Note: python will not allow a function to change a global 
# variable unless that function declares the global variable
# as shown below. If you comment out the "global min" statement
# you will find that the value of min remains 10 even after the
# changeMin function is called.

def changeMin():
	global min
	min=5
	
min=10
changeMin()
print ("min is", min)
