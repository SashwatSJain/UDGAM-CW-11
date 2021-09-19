def primefactors(n):
    while n % 2 == 0:
        print(2, end='*'),
        n /= 2
    for i in range(3,int(n**0.5)+1,2):
        while (n % i == 0):
            print(int(i), end='*')
            n /= i
    if n > 2:
        print (int(n), end='*')
    

n = int(input("n>"))
for x in range(1, n+1):
    print(x, ' : ', sep = '', end = '')
    primefactors(x)
    print('\n', '-'*20)