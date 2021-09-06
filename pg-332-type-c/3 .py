time, hours_ahead = int(input("time : ")), int(input("hrs ahead : "))

a = (time+hours_ahead)%12

print(a, ":00", sep='')