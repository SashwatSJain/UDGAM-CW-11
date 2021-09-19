# a)
print('\n-------------------------------- a --------------------------------\n')

print('a : ')
for x in range(1, 6):
    for y in range(x):
        print(chr(65+y), end=' ')
    print('')

print('\n-------------------------------- b --------------------------------\n')

# b)
for x in range(1, 6):
    for y in range(x):
        print(chr(64+x), end=' ')
    print('')

print('\n------------------------------- c ---------------------------------\n')

# c)
for x in range(1, 6):
    for y in range(x):
        print((x-1)*2, end=' ')
    print('')

print('\n------------------------------ d ----------------------------------\n')

# d)
for x in range(1, 5):
    for y in range(x):
        print(x*2, end=' ')
    print('')