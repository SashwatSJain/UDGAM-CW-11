def alphabets(n):
    for x in range(1, n+1):
        for y in range(1, x+1):
            print(chr(y+64), end='')
        print('\n')

alphabets(5)