# from math import factorial

n = int(input("Enter a  number:"))
def factorial_recursive(n):
    if(n == 1 or n== 0):
        return 1
    else:
        return n*factorial_recursive(n-1)

a = factorial_recursive(n)
print(a)