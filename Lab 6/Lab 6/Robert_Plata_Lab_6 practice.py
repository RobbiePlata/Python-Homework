# Robert Cyril Plata III
# Tip Calculator
# 10/6/2015

def calcTip(bill, tipPercent): # calculates the tip, using bill and tipPercent placeholders
    tip = bill * tipPercent
    return tip # returns the value of the tip to the program to be used later

def calcTotal (add1, add2): # Calculates up to two numbers then returns them
    finalTotal = add1 + add2
    return finalTotal # returns the finalTotal to the program to be used later

def getFloat(prompt, low, high): # The function executes the prompt
    attempts = 0
    while attempts < 1:
        try: # Try block for retrying
            userInput = input(prompt) #asks user for input
            userInput = float(userInput) #converts string to floating number
            if userInput < low:
                print("please enter a number greater than", low) # constant
                attempts = 0
            if userInput > high:
                print("please enter a number less than", high) # constant
                attempts = 0
            if userInput >= low and userInput <= high: #if following constant rules, then it goes on
                attempts = 1 #triggers the next part of the program
        except:
            print("Please enter a number")
    return userInput #returns user's input

#CONSTANTS
LOW_BILL = 1
HIGH_BILL = 500
LOW_PCT = 10
HIGH_PCT = 25

#FirstBill
firstBill = getFloat("How much was the first bill? ", LOW_BILL, HIGH_BILL)
firstTipPct = getFloat("What percent tip for the first bill?", LOW_PCT, HIGH_PCT)
firstTipPct = firstTipPct / 100
firstTip = calcTip(firstBill, firstTipPct)
final1 = calcTotal(firstBill, firstTip)
print("-------------------------------")
print("The first bill is", firstBill)
print("The tip percent is", firstTipPct)
print("The tip total is", firstTip)
print("Given a bill of "+format(firstBill,'<8,.2f'), end="")
print("The total is", final1)
print("-------------------------------")

#SecondBill
secondBill = firstBill = getFloat("How much was the second bill? ", LOW_BILL, HIGH_BILL)
secondTipPct = getFloat("What percent tip for the second bill?", LOW_PCT, HIGH_PCT)
secondTipPct = secondTipPct / 100
secondTip = calcTip(secondBill, secondTipPct)
final2 = calcTotal(secondBill, secondTip)
print("-------------------------------")
print("The first bill is", secondBill)
print("The tip percent is", secondTipPct)
print("The tip total is", secondTip)
print("Given a bill of "+format(secondBill,'<8,.2f'), end="")
print("The total is", final2)
print("-------------------------------")

#FinalTotal
finalTotal = calcTotal(final1, final2)
print("With a first total bill of "+str(final1)+" and a second total bill of "+str(final2)+" the final amount is:")
print("The combined total is", finalTotal)
