# Write a program with single infinite loop which prints 1 to 5, passes 6 to 10,
# prints 11 to 15 and terminates.

x = 0
while True:
    x+=1
    if x>0 and x<6:
        print(x)

    elif x>10 and x<16:
        print(x)

    else:
        pass