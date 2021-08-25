a = int(input("range : "))
notprime = []
prime = []
for x in range(1, a+1):
    for y in range(2,x):
        if x%y == 0:
            notprime.insert(0, x)
            break
        else:
            prime.insert(0, x)
            pass


notprime = list(dict.fromkeys(notprime))
print(notprime)
prime = list(dict.fromkeys(prime))
print(prime)