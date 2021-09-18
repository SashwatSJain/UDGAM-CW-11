l = []
while True :
    a = input("num > ")
    if a == '':
        break
    else:
        l.insert(0,int(a))

l.sort()

print("Largest Number is : ", l[-1])