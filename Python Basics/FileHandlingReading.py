# f = open("Hemant.txt","rt")
f = open("Hemant.txt","rb")
content = f.read()
print(content)
f.close()


f =open("Hemant.txt","r")
#con = f.read(3)
#If we want to iterate the content of a file
for line in f:
    print(line ,end="")
f.close()
#if we want to print different lines one by one
f = open("Hemant.txt","rt")
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
f.close()