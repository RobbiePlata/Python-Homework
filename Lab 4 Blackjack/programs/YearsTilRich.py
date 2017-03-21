balance = input("What is your initial balance?")
balance = float(balance)
goal = input("What is your goal?")
goal = float(goal)
rate = input("What is your rate of return?")
rate = float(rate)

year = 0
while balance <= goal:
    balance = balance + (balance*rate)
    year = year + 1
    print("After", year, "years, you will have", balance)
print("It will take you", year, "years.")
