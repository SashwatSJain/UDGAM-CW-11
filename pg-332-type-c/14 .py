a = int(input("num(>20) : "))

for x in range (11, a+1):
    if a<=20:
        print("input value should be less than 20.")
        break
    elif x%3==0 and x%7==0:
        print(x, " : TipsyTopsy")
    elif x%3==0:
        print(x, " : Tipsy")
    elif x%7==0:
        print(x, " : Topsy")
    else:
        print(x, " :   -")
