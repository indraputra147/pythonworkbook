#Exercise 56: Frequency to Name

"""
Write a program that reads the frequency of some radiation from the user
and displays name of the radiation as part of an appropriate message
"""

FREQ = float(input("Enter the frequency in Hz: "))

if FREQ < 3e9:
    print("Radio Waves")
elif FREQ >= 3e9 and FREQ < 3e12:
    print("Microwaves")
elif FREQ >= 3e12 and FREQ < 4.3e14:
    print("Infrared Light")
elif FREQ >= 4.3e14 and FREQ < 7.5e14:
    print("Visible Light")
elif FREQ >= 7.5e14 and FREQ < 3e17:
    print("Ultraviolet Light")
elif FREQ >= 3e17 and FREQ < 3e19:
    print("X-Rays")
elif FREQ >= 3e19:
    print("Gamma Rays")
else:
    print("Invalid input!")
