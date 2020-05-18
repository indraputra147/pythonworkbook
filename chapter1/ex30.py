#Exercise 30: Celcius to Fahrenheit and Kelvin

"""
The program reads a temperature from the user in degrees Celsius
then display the equivalent temperature in degrees Fahrenheit and Kelvin
"""
c = float(input("Input the temperaure in degrees Celsius: "))

f = (9 * c /5) + 32
k = c + 273.15

print("Output:")
print("%.2f" % f + " degree Fahrenheit ")
print("%.2f" % k + " degree Kelvin")

