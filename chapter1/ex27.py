#Exercise 27: When is Easter?
"""
The program reads the year from the user
Then display the date of Easter in that year
using Anonymous Gregorian Computus Algorithm
"""

#import math

y = int(input("Input a year: "))

a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19*a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2*e + 2*i - h - k) % 7
m = (a + 11*h + 22*l) // 451
month = (h - l - 7*m + 114) // 31
day = 1 + ((h + l - 7*m + 114) % 31)

import month_name

msg = "The date of Easter for this year is {} {}"
print(msg.format(day, month_name.mn(month)))

