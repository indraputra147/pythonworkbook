#Exercise 21: Area of a Triangle

"""
The program reads the values for base(b) and height(h) from the user
then compute and display the area of triangle
"""

b = float(input("Input the base of the triangle: "))
h = float(input("Input the height: "))

a = b * h / 2

print("The area of the triangle is %.2f" % a)
