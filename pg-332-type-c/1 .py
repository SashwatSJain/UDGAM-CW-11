l_cm = float(input("enter length in cm : "))
if l_cm<1:
    print("invalid length")

else:
    l_inch = l_cm/2.54
    print(f"{l_cm} cm is equal to {l_inch} inches")