#Exercise 14: Height Units
"""
The program reads a number of feet from the user, followed by a number of inches.
The program should compute and display the equivalent number of centimeters.
1 foot = 12 inches
1 inch = 2.54 centimeters
"""

ft = float(input("input 1, feet: "))
inch = float(input("input 2, inches: "))

cm1 = ft * 12 * 2.54
cm2 = inch * 2.54

print("output 1: %.2f" % cm1 + " cm")
print("output 2: %.2f" % cm2 + " cm")
