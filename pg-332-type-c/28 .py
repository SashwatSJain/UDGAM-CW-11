n = int(input('celcius(1) or fahrenheit(2)'))
a = int(input("temp : "))
if n == 1:
    print(a, '℃ = ', (a*1.8)+32, '℉')
elif n == 2:
    print(a, '℉ = ', (a-32)*5/9, '℃')