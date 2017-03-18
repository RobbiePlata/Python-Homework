def mySum(low,high) :
    total = 0
    for j in range(low,high+1):
        total += j
    return total

def sumAndPrint(myLow,myHigh):
    myTotal = mySum(myLow,myHigh)
    print ("the sum from", myLow, "to", myHigh, "is", myTotal)

# Main program
#lowSales = 3
#highSales = 10
sumAndPrint(lowSales,highSales)


lowGrade = 5
highGrade = 7
sumAndPrint(lowGrade,highGrade)
