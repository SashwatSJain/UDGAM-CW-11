
n = int(input("how many numbers? "))
 
o_num = []

for x in range(1, 2*n):
    if x%2 != 0:
        o_num.insert(0,x)
    else:
        pass

print(o_num)