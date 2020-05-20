#Exercise 38: Name That Shape

"""
write a program that determines the name of a shape from its number of sides
read the number of sides from the user, up to 10 sides.
if a number of sides outsides of this range, display an error message.
"""

n = int(input("Enter the number of side of a shape (up to 10): "))

if n == 1:
    print("It's a dot!")
elif n == 2:
    print("It's a line!")
elif n == 3:
    print("The Triangle.")
elif n == 4:
    print("A Square!")
elif n == 5:
    print("Pentagon!")
elif n == 6:
    print("This one is called Hexagonal.")
elif n == 7:
    print("I think it's called Septagon.")
elif n == 8:
    print("The famous Octagonal")
elif n == 9:
    print("Nonagon, isn't it?")
elif n == 10:
    print("Finally, the decagon.")
else:
    print("""
    Beeep!!!
    The input is out of range. please try again.
    """)
