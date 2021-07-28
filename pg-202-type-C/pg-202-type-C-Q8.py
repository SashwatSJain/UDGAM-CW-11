x = int(input("Height in cm : "))
inch = x / 2.54
print(int(x / 2.54/12), "feet", int(x / 2.54-(12*int(x / 2.54/12))), "inches")
