#Exercise 48: Birth Date to Astrological Sign

"""
The program will ask the user to enter his or her month and day of birth
Then report the user's zodiac sign
"""

MONTH, DAY = input("Enter your birthday: ").split()

DAY = int(DAY)

if MONTH == "December":
    print("Capricorn") if DAY >= 22 else print("Sagittarius")
elif MONTH == "November":
    print("Sagittarius") if DAY >= 22 else print("Scorpio")
elif MONTH == "October":
    print("Scorpio") if DAY >= 23 else print("Libra")
elif MONTH == "September":
    print("Libra") if DAY >= 23 else print("Virgo")
elif MONTH == "August":
    print("Virgo") if DAY >= 23 else print("Leo")
elif MONTH == "July":
    print("Leo") if DAY >= 23 else print("Cancer")
elif MONTH == "June":
    print("Cancer") if DAY >= 21 else print("Gemini")
elif MONTH == "May":
    print("Gemini") if DAY >= 21 else print("Taurus")
elif MONTH == "April":
    print("Taurus") if DAY >= 20 else print("Aries")
elif MONTH == "March":
    print("Aries") if DAY >= 21 else print("Pisces")
elif MONTH == "February":
    print("Pisces") if DAY == 19 else print("Aquarius")
elif MONTH == "January":
    print("Aquarius") if DAY >= 22 else print("Capricorn")
else:
    print("Wrong Input!")
