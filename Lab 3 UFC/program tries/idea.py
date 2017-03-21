#REQUIREMENTS
#A_CONSTANT ~done~
#2 USER NUMBERIC INPUTS 
#PERFORM SOME CALCULATION WITH THE CONSTANT AND 2 USER INPUTS ~done~
#TRY BLOCK CONTAINING ALL ~done~
#EXCEPT BLOCK ~done~
#USER SHOULD ENTER A STRING WITH 3 OR MORE CHOICES. maybe kilometer kiloliter kilogram
#IF/ELIF STRUCTURE
#include concatination if you can

CONVERSION_CONSTANT=2.2046226218

try:

    pounds=input("How many pounds")
    pounds=float(pounds)
    kg = pounds * (1 / CONVERSION_CONSTANT)
    kg = kg * 100
    kg = kg // 100
    if pounds <= 2:
        print("That wont be a full kilogram yet!")
    elif kg < 57:
        print ("You weigh "+ str(kg) +" in kilograms!")
    elif kg < 60:
        print ("You weigh "+ str(kg) +" in kilograms!")
        print ("and you are a Flyweight ")
    elif kg < 65:
        print ("You weigh "+ str(kg) +" in kilograms!")
        print ("and you are a Bantamweight ")
    elif kg < 69:
        print ("You weigh "+ str(kg) +" in kilograms!")
        print ("and you are a Featherweight  ")
    elif kg < 76:
        print ("You weigh "+ str(kg) +" in kilograms!")
        print ("and you are a Lightweight   ")
    elif kg < 83:
        print ("You weigh "+ str(kg) +" in kilograms!")
        print ("and you are a Welterweight  ")
    elif kg < 92:
        print ("You weigh "+ str(kg) +" in kilograms!")
        print ("and you are a Middleweight   ")
    elif kg < 119:
        print ("You weigh "+ str(kg) +" in kilograms!")
        print ("and you are a  Light Heavyweight ")
    elif kg >= 120:
        print ("You weigh "+ str(kg) +" in kilograms!")
        print ("and you are a Heavyweight")
except:
    print ("Enter a number, not letters!")
