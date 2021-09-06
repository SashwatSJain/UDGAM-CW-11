a, b = float(input("Num 1 : ")), float(input("Num 2 : "))

if a-b<=0.001 or b-a<=0.001:
    print("Close")

else:
    print("not close")
