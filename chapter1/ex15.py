#Exercise 15: Distance Units

"""
Input of measurements in feet
output in inches yards, and miles
"""
#input in feet from the user
ft = float(input("Measurement in feet: "))

#compute the output
inch = ft * 12
yrd = ft / 3
mile = ft / 5280

print("output:")
print("%.2f" % inch + " inches")
print("%.2f" % yrd + " yards")
print("%.5f" % mile + " miles")


