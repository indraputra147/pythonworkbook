#Exercise 29: Wind Chill

"""
The program reads the air temperature and wind speed from the user
then display the Wind Chill Index(WCI) rounded to the closest integer
"""

print("Program to compute Wind Chill Index (WCI)")
print("""
    The wind chill index is only considered valid for temperatures less
    than or equal to 10 degrees Celsius and wind speed exceeding 4.8 km/h
""" )
t = float(input("Input the temperature: "))
v = float(input("wind speed: "))

wci = 13.12 + (0.6215 * t) - (11.37 * v ** 0.16) + (0.3965 * t * v ** 0.16)
wci = round(wci)
print("The Wind Chill Index is ", wci )
