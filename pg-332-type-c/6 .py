x, y, z = int(input("Side 1 : ")), int(input("Side 2 : ")), int(input("Side 3 : "))

if x + y > z and y + z > x and z + x > y:
    print("It is a triangle")

else:
    print("It is not a triangle")