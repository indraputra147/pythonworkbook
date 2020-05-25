#Exercise 49: Chinese Zodiac

"""
The program reads a year from the user
then displays the animal associated with that year
"""

YEAR = int(input("Enter a year: "))

if (YEAR % 12) == 8:
    print("Dragon")
elif (YEAR % 12) == 9:
    print("Snake")
elif (YEAR % 12) == 10:
    print("Horse")
elif (YEAR % 12) == 11:
    print("Sheep")
elif (YEAR % 12) == 0:
    print("Monkey")
elif (YEAR % 12) == 1:
    print("Rooster")
elif (YEAR % 12) == 2:
    print("Dog")
elif (YEAR % 12) == 3:
    print("Pig")
elif (YEAR % 12) == 4:
    print("Rat")
elif (YEAR % 12) == 5:
    print("Ox")
elif (YEAR % 12) == 6:
    print("Tiger")
elif (YEAR % 12) == 7:
    print("Hare")
else:
    print("This is even not a number -_-")
