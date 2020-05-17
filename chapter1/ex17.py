#Exercise 17: Heat Capacity

"""
The Program reads the mass of the water and temperature change
q = m * C *dT
Specific heat capacity of water(c) is 4.186 J/gC
"""
print("Calculating the amount of energy...")
mass = float(input("Mass of water (in gram): "))
dT   = float(input("Change of temperature (in Celsius): "))
c    = 4.186

q = mass * c *  dT


print("The amount of energy is %.2f" % q + " joule")


print("Calculating the bill of heater...")

w = 8.9

kwh = q * 2.777e-7
cost = kwh * w

print("the bill of heater is %.5f" % cost + " cents")
