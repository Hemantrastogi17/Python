# def function1():
#     print("Hello World")
#
# func2  = function1
# del function1  #Deletes the fucntion1()
# func2()


# def fun(num):
#     if num == 0:
#         return print
#     elif num == 1:
#         return sum
#
# print(fun(1))

# Decorators


def functs(functs3):
    def functs2():
        print("Hello this is functs2")
        functs3()
        print("Exiting functs2")
    return functs2()

@functs
def Hemant():
    print("This is Hemant")

# Hemant = functs(Hemant)
