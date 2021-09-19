# a)
from math import factorial

x = int(input("x : "))

summ = 0
for i in range(1, 7):
    n = (x**i)/factorial(i)
    if i%2 == 0:
        n*=-1
    else:
        pass

    print(n)
    summ += n
    
print(summ)

# b)
n = int(input("2nd loop\nn >"))
m = int(input("x > "))
sumb = 0
for x in range(1, n+1):
    a = (m**x)/x
    sumb += a
    print(a)

print('\n', sumb, sep = '')