#Exercise 31: Units of Pressure

"""
The program reads a pressure from the user in kilo-pascals
then display the equivalent pressure in 
pounds per square inch(pound/inch^2), milimeters of mercury(mmHg) and atmosphere(atm)
"""

p = float(input("Input a pressure in kilopascals: "))

p1 = p / 6.895
p2 = p * 7.501
p3 = p / 101

print("Equivalent values: ")
print("%.2f" % p1 + " pound/inch^2")
print("%.2f" % p2 + " mmHg")
print("%.2f" % p3 + " atm")



