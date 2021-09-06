year = int(input("Year : "))
ly = None
if year%4 == 0:
    if year%100 == 0 and year%400 == 0:
        ly = True
    elif year%100 == 0 and year%400 != 0:
        ly = False
    elif year%100 != 0 and year%400 != 0:
        ly = True

else:
    ly = False

if ly:
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")