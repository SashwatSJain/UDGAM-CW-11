n = int(input("n >"))
m = int(input("m >"))
div = []
indiv = []
for i in range(1, n+1):
    if i%m==0:
        div.insert(0, i)
        if i%2==0:
            print(i, "is divisible by ", m, "and ", i, "is even")
        
        else:
            print(i, "is divisible by ", m, "and ", i, "is odd")
    else:
        indiv.insert(0,i)
        print(i, "is not divisible by ", m)

