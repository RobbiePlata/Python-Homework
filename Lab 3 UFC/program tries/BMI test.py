height=input("height in inches")
weight=input("weight in pounds")
height=int(height)
weight=int(weight)

BMI_CONSTANT=703.07

calculation = (weight/(height * height)) * BMI_CONSTANT
try:
    if calculation < 18.5:
        print ("underweight")
    elif calculation < 25:
        print ("normal")
    elif calculation < 30:
        print ("overweight")
    else:
        print ("obese")
except:
    print ("enter a number value.")
