# This program illustrates string slicing


mystr = "Hemant is a good boy"
# print(len(mystr))
# print(mystr[5])
# print(mystr[0:5])
# print(mystr[0:15:2])
# print(mystr[0:-1])
# print(mystr[::-1])  # Reverses the string
# print(mystr[::-2])
# print(mystr[-15:-1])
# print(mystr[-1:-15:-1])


print(type(mystr))
print(mystr.isalnum())
print(mystr.isalpha())


str = "Firefistisagoodboy"
print(str.isalnum())
print(str.isalpha())
print(str.endswith("boy"))
print(str.count("boy"))
print(str.capitalize())
print(str.find("o"))
print(str.upper())
print(str.lower())
print(mystr.replace("is","are"))
