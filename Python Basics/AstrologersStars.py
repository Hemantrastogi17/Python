num1 = int(input("Enter a number:"))
num2 = int(input("Choose between 1 and 0:"))

i = 1
j = 1
if num2 == 1:
    for i in range(num1):
        for j in range(num1):
            if(j<=i):
                print("*",end="")
            else:
                print(" ",end="")
        print("")
elif num2 == 0:
    for i in range(num1):
        for j in range(num1):
            if(j<num1-i):
                print("*",end="")
            else:
                print(" ",end="")
        print("")
