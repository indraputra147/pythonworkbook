#Exercise 58: Is It a Leap Year?

"""
The program reads a year from the user
displays a message indicating whether or not it is a leap year
"""

YEAR = int("Enter a year: ")

if (YEAR % 400) == 0:
    if (YEAR / 4) == 0:

