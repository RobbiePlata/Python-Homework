# Robert Cyril Plata III
# Weight Calculator
# Sally Kyvernitis
# 10/6/2015

#calcKg does conversion
def calcKg(lbs, constant): # calculates the weight and formats it.
    kg = lbs * (1 / constant)
    kg = kg * 100
    kg = kg // 100
    return kg

#getFloat tells the user if the number is too high or too low for this program.
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

#getTotal is getting the total after subtraction of the calculation variables
def getTotal(prompt1, weight):
    attempts = 0
    while attempts < 1:
        try:
            lose = input(prompt1)
            lose = float(lose)
            total = weight - lose
            attempts += 1
        except:
            print("Enter a number")
    return total

# CONSTANTS
LOW = 50
HIGH = 600
KGCONSTANT = 2.2046226218

#Calculating KG from LBS
getWeight = getFloat("How much do you weigh in lbs?", LOW, HIGH)
kg = calcKg(getWeight, KGCONSTANT)
print("You weigh",kg," in kilograms.")
print("------------------------------------")

#Calculating pounds lost, then converting pound loss total to kilograms.
calculation = getTotal("How many pounds do you want to lose.", getWeight)
conversion = calcKg(calculation, KGCONSTANT)
print("You will weigh", conversion, "kilograms after losing that weight in pounds.")

