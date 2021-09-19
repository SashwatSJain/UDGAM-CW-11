#Program to find whether a number is prime or composite

def isPrime(number):
    p = None
    for y in range(1, number//2+1):
        if number % y == 0 and p:
            p = False
            break

        else:
            p = True
    return p

num = int(input(">>>>"))

if isPrime(num):
    print("The number is prime")
elif num<2:
    print("The number is neither prime nor composite")
else:
    print("The number is composite")