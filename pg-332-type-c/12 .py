x, y, z = int(input("s1 : ")), int(input("s2 : ")), int(input("s3 : "))

if x+y<=z or y+z<=x or x+z<=y:
    print("it is not a triangle")

elif x == y and x==z:
    print("it is an equilateral triangle")

elif x*x == (y*y)+(z*z) or y*y == (z*z)+(x*x) or z*z == (x*x)+(y*y):
    print("it is a right angle triangle")

elif x==y or y==z or z==x:
    print("it is an isosceles triangle")

else:
    print("it is a scalene triangle")