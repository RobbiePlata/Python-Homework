# Get user input
unitPrice=input("What was the price of the item you bought? ")
qty=input("How many did you buy? ")

# convert string input to numbers
unitPrice=float(unitPrice)
qty=int(qty)

# calculate
totalPaid=unitPrice*qty

# output results
print ("You paid", totalPaid, "for", qty, "items today.")
