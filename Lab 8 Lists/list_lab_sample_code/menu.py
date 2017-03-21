def menu():
	while True:
		print()
		print("1. do this")
		print("2. do that")
		print("3. do something else")
		print("4. exit")
		choice=input("Please enter your choice: ")
		try:
			choice=int(choice)
			if (choice>=1 and choice <=4):
				return choice # user gave good input, so return that
			else:
				print ("Enter a number between 1 and 4")
		except:
			print("Enter a number")
			
# MAIN PROGRAM

mychoice=menu()
print("your choice was", mychoice)