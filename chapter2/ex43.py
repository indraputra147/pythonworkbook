#Exercise 43: Frequency to Note

"""
Program reads a frequency from the user
If the frequency is listed in the table, report the name of the corresponding note
otherwise, report that the frequency does not correspond to a known note
There is no need to consider notes from other octaves
"""

FREQ = float(input("Enter a frequency of a note: "))

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

if FREQ == 261.63:
    print("C4")
elif FREQ == 293.66:
    print("D4")
elif FREQ == 329.63:
    print("E4")
elif FREQ == 349.23:
    print("F4")
elif FREQ == 392.00:
    print("G4")
elif FREQ == 440:
    print("A4")
elif FREQ == 493.88:
    print("B4")
else:
    print("The frequency does not correspond to a known note!")
