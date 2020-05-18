#Exercise 23: Area of a Regular Polygon

"""
Write a program that reads length of a side(s) and n number of sides from the user 
then displays the area of a regular polygon constructed from these values.
"""

n = int(input("Enter the number of sides of polygon: "))
s = float(input("Enter the length of the side of polygon: "))

import math

a = (n * s * s) / (4 * math.tan(math.pi / n))

print("The area of the polygon is %.2f" % a)
