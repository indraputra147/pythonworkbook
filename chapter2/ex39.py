#Exercise 39: Month Name to Number of Days

"""
Program reads the name of a mont from the user as a string
display the number of days in that mont
"""

month = input("Enter the name of a month: ")

day30 = ['April', 'June', 'September', 'November']
day31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']

if month in day30:
    print("30 days!")
elif month in day31:
    print('31 days!')
elif month == 'February':
    print("28 or 29 days")
else:
    print("wrong input!")
