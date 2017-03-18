#Robert Cyril Plata III
#9/1/2015
#Lab 2 Calc
#This program calculates your revenue, and profit after tax. It also tells you to spend 20% of your money somewhere.
#Professor Sally Kyvernitis

SELFISH_MONEY = .20 #Simple constant

#This is the name of the product being sold.
productName = input("What is the name of your product?")#I don't NEED the try clause for this.
print ("How much does", productName,"cost?")
#This is the price of the product
try: #User will attempt to enter a number.
    x=price = input()#User input. I made it equal to x, because it is a user input, and I want to tell the user it is wrong in exception clause.
    price = float(price)#Floating number for decimals.
    x=quantity = input("How much product did you sell?") #User input for quantity. Made it equal to X for exception clause.
    quantity = int(quantity) #Quantity is an integer because you aren't going to sell part of a product.
    income = (quantity) * (price)
    print ("You made",income, "for selling", quantity,"products.")
    x=bizCosts = input("What are the costs to run your business? ") #Business costs of employees, production ect. Made it equal to X for exception clause.
    bizCosts = float(bizCosts)#It can be a number with decimals.
    beforeTax = income - bizCosts #income - bizCosts before tax is deducted
    beforeTax = float(beforeTax)
    print ("After business expenses, you have", beforeTax,"dollars.")
    x=tax = input("What is the income tax percentage in your state? ")#input for tax percentage. Made it equal to X for exception clause.
    tax = int(tax)#tax is an integer, not float. Made it equal to X for exception clause.
    realTax = tax * .01 #makes the tax percentage a decimal. It multiplies beforeTax by a decimal.
    afterTax = beforeTax * realTax #this is the tax
    finishedTax = beforeTax - afterTax #this is the tax deducted from the income of the user.
    print ("After tax, you have made a profit of",finishedTax,"dollars after selling",quantity,productName,"(s)!") #Telling user their profit after income tax.

except: #User didn't enter a number or a string tried to multiply with an integer.
    print (x," is not a number. Restart the program.") #In case user types a non number.
    
buysomethingNice = finishedTax * SELFISH_MONEY
print ("Go spend 20% of your profit..", buysomethingNice, "at a casino. You earned it")
print ("")
print ("Have a good day")
