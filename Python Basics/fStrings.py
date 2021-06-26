import math
me = "Hemant"
a1 = "here"
a = "This is %s %s"%(me,a1)
print(a)


str = "Hello {} {}"
str1 = str.format(me,a1)
print(str1)

#F Strings
a  = f"This is {me} {a1} {math.cos(90)}"
print(a)
