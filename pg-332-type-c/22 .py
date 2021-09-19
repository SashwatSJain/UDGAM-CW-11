# 26-35, 36-45, 46-55
a, b, c = 0, 0, 0
i = 0
n = int(input("number of employees : "))
for x in range(n):
    age = int(input(f"age of employee {x+1} : "))
    if 56>age>45:
        c+=1
        pass
    elif 46>age>35:
        b+=1
        pass
    elif 36>age>25:
        a+=1
        pass
    else:
        print("too young or too old to work")
        i+=1

print(f"\n\n26-35 : {a} employees\n36-45 : {b} employees\n46-55 : {a} employees\ntoo young/too old : {i} employees")