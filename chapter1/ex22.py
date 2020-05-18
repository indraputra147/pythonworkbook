#Exercise 22: Area of a Triangle (Again)

"""
The program reads the lengths of the 3 sides of a triangle from the user
then displays its area
"""

import math

s1, s2, s3 = input("Input the 3 sides  of the triangle separated by space: ").split()

s1 = float(s1)
s2 = float(s2)
s3 = float(s3)

s = (s1 + s2 + s3) / 2

a = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

print("The area of the triangle is %.2f" % a)
