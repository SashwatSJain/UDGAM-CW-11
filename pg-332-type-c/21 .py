from math import factorial
x = int(input(""))
summ = 1.0
print(summ)
for i in range(1, x+1):
    n = 1/factorial(i)
    if i%2 == 0:
        n*=-1
    else:
        pass

    print(n)
    summ += n
    
print(summ)