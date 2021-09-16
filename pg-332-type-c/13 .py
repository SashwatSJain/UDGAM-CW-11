# Write a program to take an integer a as an input and check whether it ends with 4 or 8.
#  if it ends with 4 print "ends with 4", if it ends with 8, print "ends with 8", otherwise print "ends with neither"

a = str(int(input(">>>")))
# a = str(a)
if a[-1] == '4'or a[-1]=='8':
    print('ends with ', a[-1])
else:
    print('ends with neither 4 nor 8')