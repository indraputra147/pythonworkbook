#Exercise 24: Units of Time

"""
Create a program that reads a duration from the user as a number of days, hours,
minutes and seconds.
Then compute and display the total number of seconds represented by the duration
"""
print("Input the duration ")
d = int(input("Days: "))
h = int(input("Hours: "))
m = int(input("Minutes: "))
s = int(input("Seconds: "))

total = (d * 24 * 3600) + (h * 3600) + (m * 60) + s

print("The total duration is", total,"seconds")
