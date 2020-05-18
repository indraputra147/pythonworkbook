#Exercise 28: Body Mass Index

"""
The program reads a height and wight from the user
then compute the Body Mass Index(BMI) and displaying it
"""

print("") 

h = float(input("Input a height: "))
w = float(input("Input a weight: "))

bmi1 = (w * 703) / (h * h) #for height and weight in inches

bmi2 = w / (h * h) #for height and weight in meters



