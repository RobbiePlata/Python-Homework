def printTemple(howManyTimes, withPoint):
    for i in range (0, howManyTimes):
        print("Temple")
        if (withPoint):
            print ("!")
        else:
            print("")
def main():
    printTemple(3, True)

main()