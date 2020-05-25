#Exercise 47: Season from Month and Day

"""
The program reads a month as a string and day as an integer from the user
Then display the season associated with the date that was entered
"""

MONTH = input("Enter the name of a month: ")

DAY = int(input("Enter the date: "))

if MONTH == "March" and DAY == 20:
    print("It was first day of Spring!")
elif MONTH == "June" and DAY == 21:
    print("Here comes the Summer!")
elif MONTH == "September" and DAY == 22:
    print("First day of Fall!")
elif MONTH == "December" and DAY == 21:
    print("The winter is coming!")
else:
    print("The date you was entered is not associated with any specific day!")

