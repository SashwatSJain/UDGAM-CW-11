a = int(input("range : "))
notprime = []
prime = []
for x in range(1, a+1):
    for y in range(2,x):
        if x%y == 0:
            prime.update(x)
            break
        else:
            notprime.update(x)
            pass

print(prime, notprime)