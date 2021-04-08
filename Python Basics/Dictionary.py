#This program illustrates used od Dictionary

#Dictionary is nothing but a set of key value pairs
d1 = {"Hemant":"Momos",
      "Harshit":"Paneer","Yatin": "Noodles",
      "Ritvik":{"Breakfast": "Maggi", "Lunch": "Dal Roti","Dinner": "Chinese"}}
print(d1["Hemant"])
print(d1["Ritvik"]["Breakfast"])
print(d1)
del d1["Hemant"]
print(d1)
d2 = d1.copy()
d3 = d1 #d3 is a pointer which points at an already existing dictionary no new copy of d1 is created here
#Any changes made in d3 will directly affect d1


print(d2.get("Harshit"))
d2.update({"Hemant":"Momos"})
print(d2)
print(d2.keys())
print(d2.items())