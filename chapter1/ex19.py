#Exercise 19: Free Fall

"""
Create a program that determines how quickly an object is traveling
when it hits the ground
The program reads the height in meters (m) as an input
"""

import math

h = float(input("Enter the height from which the object is dropped in meters: "))
a = 9.8

vf = math.sqrt(2 * a * h )

print("The final speed of the object is %.2f" % vf + " m/s")
