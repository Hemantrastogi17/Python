 # Lambda Fucntions or Anonymous functions

# def add(a , b):
#      return a+b

add =  lambda x,y: x+y

print(add(3,4))

# def a_first(a):
#     return a[0]

a = [[1,2],[17,15],[12,4]]
a.sort(key=lambda a:a[1])
print(a)