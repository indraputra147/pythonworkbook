#Exercise 45: Date to Holiday Name

"""
The program reads a month and day from the user
If the month and day match one of the holidays listed previously,
then display the holiday's name
"""

MONTH = input("Enter a name of the month: ")
DAY = int(input("Enter the date: "))

if MONTH == "January" and DAY == 1:
    print("It's a New Year's Days!")
elif MONTH == "July" and DAY == 1:
    print("It's a Canada Day!")
elif MONTH == "December" and DAY == 25:
    print("It's a Christmas Day!")
else:
    print("The entered month and day do not correspond to a fixed-date holiday in Canada!")
