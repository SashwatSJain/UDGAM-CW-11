'''Python Program to check if a number is a Perfect number.
A perfect number is a positive integer that is equal to the sum of its
proper positive divisors except itself
A perfect number is a number that is half the sum of all of its positive
divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are
its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6
is equal to half the sum of all its positive divisors:
(1+2+3+6) /2=6.
The next perfect number is 28 = 1 + 2 + 4 + 7 + 14.
This is followed by the perfect numbers 28, 496, 8128, and 33550336.'''

num = int(input("Number : "))
sum = 0

for x in range(1, num):
    if num%x == 0:
        sum += x
    else:
        pass

if sum == num:
    print("y")

else:
    print("n")