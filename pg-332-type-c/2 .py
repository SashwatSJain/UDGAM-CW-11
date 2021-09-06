qty = int(input("how many products are you buying?"))

if qty<10:
    print("total cost : ₹", qty*120)

elif qty<100:
    print("total cost : ₹", qty*100)

else:
    print("total cost : ₹", qty*70)
    