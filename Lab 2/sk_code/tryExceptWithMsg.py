x=input("Please enter a number: ")
try:
    i=int(x)
    print ("numeric value is ", i)
except Exception as err:
    print ("exception ",x, " is not a number")
    print (" detailed message:", err)
