#EXercise 25: Units of Time (Again)

"""
The program is reverse process of the Exercise 24
Reads a number of seconds from the user
Then displays in the form D:HH:MM:SS
"""

s = int(input("Enter the number of seconds: "))

d = s // 86400
h = (s % 86400) // 3600
m = (s % 86400 % 3600) // 60
s = s % 86400 % 3600 %

