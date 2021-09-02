# greatest and smallest value out of 3 values

a, b, c = int(input("Num 1 : ")), int(input("Num 2 : ")), int(input("Num 3 : "))

if a>b and a>c:
    print(f"{a} is the greatest value")
    if c<b:
        print(f"{c} is the smallest value")
    else:
        print(f"{b} is the smallest value")

elif b>a and b>c:
    print(f"{b} is the greatest value")
    if c<a:
        print(f"{c} is the smallest value")
    else:
        print(f"{a} is the smallest value")

else:
    print(f"{c} is the greatest value")
    if a<b:
        print(f"{a} is the smallest value")
    else:
        print(f"{b} is the smallest value")

    