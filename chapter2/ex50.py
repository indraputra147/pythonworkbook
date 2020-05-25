#Exercise 50: Richter Scale

"""
The program reads a magnitude from the user
then displays the appropriate descriptor as part of a meaningful message
"""

MAGNITUDE =  float(input("Enter a magnitude: "))

if MAGNITUDE < 2.0:
    print("Micro Earthquake")
elif MAGNITUDE >= 2.0 and MAGNITUDE < 3.0:
    print("Very Minor Earthquake")
elif MAGNITUDE >= 3.0 and MAGNITUDE < 4.0:
    print("Minor Earthquake")
elif MAGNITUDE >= 4.0 and MAGNITUDE < 5.0:
    print("Light Earthquake")
elif MAGNITUDE >= 5.0 and MAGNITUDE < 6.0:
    print("Moderate Earthquake")
elif MAGNITUDE >= 6.0 and MAGNITUDE < 7.0:
    print("Strong Earthquake")
elif MAGNITUDE >= 7.0 and MAGNITUDE < 8.0:
    print("Major Eartquake")
elif MAGNITUDE >= 8.0 and MAGNITUDE < 10.0:
    print("Great Earthquake")
elif MAGNITUDE >= 10.0:
    print("Meteoric Earthquake!")
else:
    print("Wrong input dude!")
