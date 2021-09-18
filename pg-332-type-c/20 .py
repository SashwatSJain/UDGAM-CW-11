# a)
x = 2
a, b, da, db = 2, 9, 3, 4

for i in range(1, 8):
    x+=1
    if x % 2 == 0:
        print('-',a,'/', b)
        a+=da
        b+=db
    else:
        print(' ', a,'/', b)
        a+=da
        b+=db

print("next loop")

# b)

n = int(input("n : "))
for x in range(1, n+1):
    print(x**2)