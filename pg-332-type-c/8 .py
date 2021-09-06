def isPrime(number):
    p = None
    for y in range(1, number//2+1):
        if number % y == 0 and p:
            p = False
            break

        else:
            p = True
    return p


a = int(input(">>>"))
b = a**0.5
if  b-int(b)==0:
    b = int(b)
    if isPrime(b):
        print(b, "is a prime number")
    else:
        print(b, "is not a prime number")
else:
    print(b, "is not a prime number")