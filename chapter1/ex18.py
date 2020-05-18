#Exercise 18: Volume of a Cylinder

"""
Write a program that reads the radius of the cylinder along with its height
then computes its volume, display the result rounded to one decimal place
"""

import math

r = float(input("Input the radius of cylinder: "))
h = float(input("Input the height: "))

v = math.pi * r * r * h

print("The volume of the cylinder is %.1f" % v)
