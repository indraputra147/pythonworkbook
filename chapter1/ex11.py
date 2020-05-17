#Exercise 11: Fuel Efficiency
"""
Convert from miles-per-gallon(MPG) to liters-per-hundred(L/100 km)
1 miles = 1.6 km
1 gallon = 3.785 liter
"""
mpg = float(input("Input the Fuel Efficiency in MPG: "))

lph = (3.785 * 100) / (mpg * 1.6)

print("The Fuel Efficiency is %.2f" % lph + " L/100 km")
