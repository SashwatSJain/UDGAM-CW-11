# WAP with single infinite loop to input nos. till user says 'Y' to continue and
# prints their sum.

sum, num = 0, 0
while True:
    num += 1
    sum += num
    print(num)
    a = input('>>>(y to print sum and terminate)')
    if str(a) != "y":
        pass
    else:
        # the print(sum) line can be put outside the loop also to get the same output
        print(sum)
        break

"""
output:
1
>>>
2
>>>
3
>>>
4
>>>y
10
"""