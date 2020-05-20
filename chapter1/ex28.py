#Exercise 28: Body Mass Index

"""
The program reads a height and weight from the user
then compute the Body Mass Index(BMI) and displaying it
"""

c = input("""
    BMI Calculator
    (a) if you input the height in inches and weight in pounds
    (b) if you input the height in meters and weight in kilograms
    Choose "a" or "b" : 
    """) 

if c == "a":
    h = float(input("Input a height (in inches): "))
    w = float(input("Input a weight (in pounds): "))

    bmi1 = (w * 703) / (h * h) #formula for height and weight in inches
    
    print("The Body Mass Index is %.1f" % bmi1)
elif c == "b":
    h = float(input("Input a height (in meters): "))
    w = float(input("Input a weight (in kilograms): "))

    bmi2 = w / (h * h) #for height and weight in meters
    print("The Body Mass Index is %.1f" % bmi2)
else:
    print("Invalid choice! Please re-rerun the program.")

