#Exercise 5: Bottle Deposits
print("""
Small drink container holding one liter or less have a $0.10 deposit
Large drink container holding more than one liter have a $0.25 deposit
""")
s = 0.10 #$0.10 deposit for <= 1 liter
l = 0.25 #$0.25 deposit for > 1 liter
sb = int(input("Input the number of small container: "))
lb = int(input("Input the number of big container: "))
ts = sb * s
tl = lb * l
t = ts + tl
print("The refund is from the containers is $%.2f " % t)
