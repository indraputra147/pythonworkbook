#Exercise 41: Classifying Triangles

"""
The program reads the length of the three sides of a triangle from the user
display a message that states the triangle's type
equilateral or isosceles or scalene
"""

print("Enter the three sides of a triangle!")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == b == c:
    print("The triangle is Equilateral")
elif a == b or b == c or a == c:
    print("The triangle is Isosceles")
else:
    print("The triangle is Scalene")
