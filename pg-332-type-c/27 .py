a, b, c, l = int(input("n1 : ")), int(input("n2 : ")), int(input("n3 : ")), []
l.insert(0,a)
l.insert(0,b)
l.insert(0,c)
l.sort()
print(f'smallest num : {l[0]}\nnext highest number : {l[1]}\nlargest number : {l[2]}')