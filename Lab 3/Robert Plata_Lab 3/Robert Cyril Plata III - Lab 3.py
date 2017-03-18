#Robert C. Plata III Lab 3 9/11/2015
#Professor Sally Kyvernitis
#REQUIREMENTS                                                   ~done~
#A_CONSTANT                                                     ~done~
#2 USER NUMBERIC INPUTS                                         ~done~
#PERFORM SOME CALCULATION WITH THE CONSTANT AND 2 USER INPUTS   ~done~
#TRY BLOCK CONTAINING ALL                                       ~done~
#EXCEPT BLOCK                                                   ~done~
#USER SHOULD ENTER A STRING WITH 3 OR MORE CHOICES.             ~done~
#IF/ELIF STRUCTURE                                              ~done~
#include concatination if you can                               ~done~

CONVERSION_CONSTANT=2.2046226218
    
try: #Trying code
    
    age=input("what is your age")# user inputs age
    age=int(age)#age is integer
    yearsUntil = 18 - age#years left until 18
    if age >= 18:#if over 18, continue program
        print ("You can compete! Do you like fighting?")#indentation for the program if user over 18
        answer=input("Yes, No, or I dont know")#question
        answer=answer.upper()   #make all upper
        answer=answer.strip()   #make all spaces outside disappear
        if answer == "YES":     #the answer is yes, indent and allow to program to go on
            print ("Great!")    #Great print
            pounds=input("How much do you weigh in pounds?")#user pounds input
            pounds=float(pounds)#pounds is floating number
            kg = pounds * (1 / CONVERSION_CONSTANT)#math for kilograms with constant
            kg = kg * 100#kg times 100
            kg = kg // 100#kg integer division answer is now not a long decimal
            if pounds <= 2:#pounds under 2 is not a full kg 
                print("That wont be a full kilogram yet!")
            elif kg < 57:
                print ("You weigh "+ str(kg) +" in kilograms!")#these are all outcomes for the kilogram number
            elif kg < 60:
                print ("You weigh "+ str(kg) +" in kilograms!")
                print ("You are a Flyweight ")
            elif kg < 65:
                print ("You weigh "+ str(kg) +" in kilograms!")
                print ("and you are a Bantamweight ")
            elif kg < 69:
                print ("You weigh "+ str(kg) +" in kilograms!")
                print ("You are a Featherweight  ")
            elif kg < 76:
                print ("You weigh "+ str(kg) +" in kilograms!")
                print ("and you are a Lightweight")
            elif kg < 83:
                print ("You weigh "+ str(kg) +" in kilograms!")
                print ("and you are a Welterweight  ")
            elif kg < 92:
                print ("You weigh "+ str(kg) +" in kilograms!")
                print ("You are a Middleweight")
            elif kg < 119:
                print ("You weigh "+ str(kg) +" in kilograms!")
                print ("You are a  Light Heavyweight ")
            elif kg >= 120:
                print ("You weigh "+ str(kg) +" in kilograms!")
                print ("You are a Heavyweight")

        elif answer == "NO":
            print ("oh that's too bad.")#doesnt continue the program, indent aligns with multiple choice
        elif answer == "I DONT KNOW":#doesnt continue the program, indent aligns with multiple choice
            print ("Learn more about it")
        else:
            print("no option for that")#if user doesnt enter an option listed
    else:
        print("Darn you aren't over 18! You have " + str(yearsUntil) +" years until you can compete.")#user enters a number lower than 18, and this aligns with first question
except Exception as error:
    print ("Enter a number, not letters!")#user enters a string instead of number
    print (error)
