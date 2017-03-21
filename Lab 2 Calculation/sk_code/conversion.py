num=27
num=num+1
print("1. The value of num is", num) # this works

msg = "2. The value of num is " + str(num)# this works
print (msg)
# converts the number to string, then concatenates the strings

num2="27"
num2=int(num2)

print ("3. The value of num is " + num) # gives error
# error is: Can't convert 'int' object to str implicitly




