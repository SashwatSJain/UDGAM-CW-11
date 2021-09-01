a = {1:"orange", 2:"banana", 3:"chikoo", 4:"grapes", 5:"exit"}

while True:
    print(a)
    b = int(input(">>>"))
    try : 
        if b == 5:
            break

        else:
            print(a[b])

    except:
        print(f"{b} is an invalid value")