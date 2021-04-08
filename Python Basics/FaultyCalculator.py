op = input("Enter the operator:")
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if(op == "*"):
    if((num1== 45 and num2== 3) or (num2==45 or num1 ==3)):
        print("555")
    else:
        print(num1*num2)
elif op=="+":
    if ((num1 == 56 and num2 == 9) or (num2 == 56 or num1 == 9)):
        print("77")
    else:
        print(num1 + num2)
elif op=="/":
    if ((num1 == 56 and num2 == 6) or (num2 == 56 or num1 == 6)):
        print("4")
    else:
        print(num1 / num2)
elif op=="-":
    print(num1-num2)