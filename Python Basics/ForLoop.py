list = [1,2,4,"String",8,11]
for item in list:
    if(type(item) == int):
        if(item>6):
            print("Item greater than 6")
        else:
            print("Item smaller than or equal to 6")

    else:
        print("Item not an integer")