#The normal argument should always be passed before *args otherwise it will give an error
def function1(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(f"{key} is a {value}")

list = ["Hemant","Firefist","Harshit","Yatin","Ritvik"]

dict = {"Hemant":"Student","Firefist":"Engineer","Harshit":"Jeweller"}
function1("This is a normal statement",*list, **dict)
