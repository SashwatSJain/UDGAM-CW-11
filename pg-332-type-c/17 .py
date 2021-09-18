# to check if a number is a palindrome number

a = input("number : ")
l = int(len(a))
n = l//2

for x in range(1, n+1):
    if a[x-1] == a[-1*x]:
        pass
    else:
        print('not a palindrome number')
        break
else:
    print("it is a palindrome number")
