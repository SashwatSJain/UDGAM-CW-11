l = []
sum = 0
while True:
    num = input('num(press enter to exit loop) : ')
    if num == '':
        break
    else:
        l.insert(0,int(num))
        
for x in range(len(l)):
    sum+=l[x]

print('average : ', sum/len(l))