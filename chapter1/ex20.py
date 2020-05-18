#Exercise 20: Ideal Gas Law

"""
Program to computes the amount of gas in moles when the user supplies
the pressure(P) in Pascals, volume(V) in liters and temperature(T) in degress Kelvin.
"""

p = float(input("Enter the pressure in Pascals: "))
v = float(input("Enter the volume in liters: "))
t = float(input("Enter the temperature in Celsius: "))
r = 8.314

tk = t + 273.15

n = (p * v) / (r * tk)

print("The number of moles of gas is %.2f" % n + " moles")

