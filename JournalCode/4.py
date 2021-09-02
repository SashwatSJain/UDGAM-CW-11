d, n = int(input("d : ")), int(input("n : "))

x = 1

for y in range(1, n+1):
    x += d*y

print(x)