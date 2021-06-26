l = 10
def function(n):
    global l
    l = l + 10
    print(n,l)

function("this is me")
print(l)


def hemant():
    x = 10
    def firefist():
        global x  # Created a global variable
        x = 100 # This did not change the value of x in hemant()
    print("Before calling firefist()",x)
    firefist()
    print("After calling firefist()",x)

hemant()
print(x) # this is the global vaala x which was created in firefist()