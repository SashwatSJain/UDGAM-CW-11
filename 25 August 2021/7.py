a, c = int(input("a : ")), int(input("l : "))
b = 0
for x in range(a, c+1):
    print(x)
    b=b+x

print("sum : ", b)