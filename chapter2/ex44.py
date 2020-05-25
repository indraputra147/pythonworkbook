#Exercise 44: Faces on Money

"""
The program reads the denomination of a banknote
then display the name of individual that appears on the banknote of the entered amount
"""

DENO = int(input("Enter the denomination of a banknote in dollar: "))

if DENO == 1:
    print("George Washington")
elif DENO == 2:
    print("Thomas Jefferson")
elif DENO == 5:
    print("Abraham Lincoln")
elif DENO == 10:
    print("Alexander Hamilton")
elif DENO == 20:
    print("Andrew Jackson")
elif DENO == 50:
    print("Ulysses S. Grant")
elif DENO == 100:
    print("Benjamin Franklin")
else:
    print("There no such note exists!")
