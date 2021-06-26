import time
k = 0
initial = time.time()
while(k<10):
    print(f"Value of k is {k}")
    k+=1

print(f"While loop ran in {time.time()-initial} seconds" )

initial2 = time.time()

for k in range(10):
    print(f"Value of k is {k}")

print("For loop ran in", initial2 - time.time()," seconds" )



localtime = time.asctime(time.localtime(time.time()))
print(localtime)