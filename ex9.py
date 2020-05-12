#Excercise 9: Compound Interest
"""
Program to compute the amount in the saving after 1,2, and 3 years.
with 4 percent of interest. Rounded to 2 decimal places.
"""

depo = int(input("Amount of money deposited into the account (in Rupiah): "))
y1 = depo + (depo * 0.04)
y2 = y1 + (y1 * 0.04)
y3 = y2 + (y2 * 0.04)

print("Amount of saving after:")
print("year 1 = Rp.%.2f" % y1)
print("year 2 = Rp.%.2f" % y2)
print("year 3 = Rp.%.2f" % y3)
