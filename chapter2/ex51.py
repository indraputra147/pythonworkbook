#Exercise 51: Roots of a Quadratic Function

"""
Write a program that computes the real roots of a quadratic function
The program should begin by prompting the user for values of a, b and c.
Then it should display a message indicating the number of real roots,
along with the values of the real roots (if any)
"""

import math

print("Suggest, you have a quadratic equation ax^2 + bx + c = 0")
print("Enter the constants a, b and c")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

D = (b**2) - (4 * (a * c))

if D < 0:
    print("The equation does not have any real roots")
elif D == 0:
    print("The equation has one real root:")
    ROOT = (-b + math.sqrt(D)) / (2 * a)
    print(ROOT)
elif D > 0:
    print("This equation has two real roots: ")
    ROOT1 = (-b + math.sqrt(D)) / (2 * a)
    ROOT2 = (-b - math.sqrt(D)) / (2 * a)
    print(ROOT1, "and", ROOT2)
else:
    print("wrong input!")
