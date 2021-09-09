
l, n = [1], 1

while n <= 40:
    n+=3
    l.insert(0,n)

l.sort()
print(l)