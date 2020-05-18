#Exercise 33: Sort 3 Integers

"""
The program reads three integers from the user
then display them in sorted order, from smallest to largest
"""

x, y, z =input("input 3 integers separated by space: ").split()

x1 = min(int(x), int(y), int(z))
x3 = max(int(x), int(y), int(z))

x2 = int(x) + int(y) + int(z) - x1 - x3

sorte = "{} {} {}"
print(sorte.format(x1, x2, x3))
