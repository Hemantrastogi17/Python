num1 = input("Enter a number:")
num2= input("Enter a number:")
try:
    sum = int(num1) + int(num2)
    print(sum)
except Exception as e:
    print(e)