def max(num1,num2):
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result
def main():
    i = 1000
    j = 2000
    k = max(i, j)
    print("The max between", i, "and", j, "is", k)

main()