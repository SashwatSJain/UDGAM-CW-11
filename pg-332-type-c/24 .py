# a)
for x in range(1, 4):
    n = 3-x
    print(' '* n + '* ' * x)

for x in range(1, 4):
    n = 3-x
    print(' '* x + '* ' * n)

# b)
for x in range(1, 4):
    print('* ' * x)

for x in range(1, 4):
    n = 3-x
    print('* ' * n)

# c)
for x in range(1, 4):
    n = 3-x
    if x==1:
        print(' '* n + '*' + ' '*n)
    elif x==2:
        print(' '+'*' + ' ' + '*')

    else:
        print('*' + ' '*x + '*')

for x in range(1, 4):
    n = 3-x
    print(' '* x + '* ' * n)

# d)
for x in range(7):
    t = x-1
    print('*', end='')
    if x==0:
        # print('')
        pass
    elif x<4:
        print(' '* t, '*', sep = '', end='')
    elif x<6:
        r = 5-x
        print(' '*r,'*',  end = '', sep = '')
    else:
        pass
    print('')