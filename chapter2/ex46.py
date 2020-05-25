#Exercise 46: What Color Is That Square?

"""
The program reads a position from the user in 8 x 8 chess board
Then report the color of the square in that row
e.g. a1 = black, d5 = white
"""

POSIT = input("Enter the position: ")

x = ord(POSIT[0])

y = int(POSIT[1])

z = (x + y) % 2

if z == 0:
    print("The square is black")
elif z == 1:
    print("The square is white")
else:
    print("Wrong Input!")
