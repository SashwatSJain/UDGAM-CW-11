n = int(input("lines : "))
n+=1
for x in range(n):
    for y in range(x):
        print("@", end="")
    print("")