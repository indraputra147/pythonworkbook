#Exercise 12: Distance Between Two Points on Earth

"""
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth's Surface.
"""

import math

print("First point coordinate:")
t1 = math.radians(float(input("latitude: ")))
g1 = math.radians(float(input("longitude: ")))

print("Second point coordinate:")
t2 = math.radians(float(input("latitude: ")))
g2 = math.radians(float(input("longitude: ")))

dist = (6371.01 * math.acos(math.sin(t1)) * math.sin(t2)) + (math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

print("The distance between these points is %.2f" % dist + " km")
