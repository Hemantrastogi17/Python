tup = (1,2,3,4,5,6,7,8,9)

def isGreaterThan5(num):
    return num > 5

tup1 = tuple(filter(isGreaterThan5 , tup))
print(tup1)