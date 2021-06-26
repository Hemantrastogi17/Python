lst = ["1","2","3"]

# for i in range(len(lst)):
#     lst[i] = int(lst[i])


# The above for loop can be replaced by map function

lst = list(map(int, lst))
lst[1]+=1
print(lst[1])


numbers = [1,2,3,4,5,6]
#  Now I want to create a list that contains sqaures of all the numbers
squares = list(map(lambda x : x*x ,numbers))
print(squares)


def square(a):
    return a*a;

def cube(a):
    return a*a*a;

func = [square,cube]

for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)