#Area and Volume

"""
Program reading a radius as an input
compute the area and volume of the circle
"""

import math

radius = float(input("The radius: "))

area = math.pi * radius * radius

volume = 4 * math.pi * radius**3 / 3

print("Area of circle is %.2f" % area)
print("The volume of the sphere %.2f" % volume)

