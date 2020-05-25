#Exercise 42: Note to Frequency

"""
The program reads the name of a note from the user
then display the note's frequency
"""

NOTE = input("Enter the name of a note: ")


"""
"The Simple Version"

if Note == "C4":
    print("261.63 Hz")
elif Note == "D4":
    print("293.66 Hz")
elif Note == "E4":
    print("329.63 Hz")
elif Note == "F4":
    print("349.23 Hz")
elif Note == "G4":
    print("392.00 Hz")
elif Note == "A4":
    print("440.00 Hz")
elif Note == "B4":
    print("493.88 Hz")
else:
    print("Wrong Input! The note must be one of C0 to C8!")
"""

#Complex Version

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

if NOTE[0] == "C":
    x = int(NOTE[1:])
    FREQ = C4 / (2 ** (4 - x))
    print("%.2f" % FREQ + " Hz")
elif NOTE[0] == "D":
    x = int(NOTE[1:])
    FREQ = D4 / (2 ** (4 - x))
    print("%.2f" % FREQ + " Hz")
elif NOTE[0] == "E":
    x = int(NOTE[1:])
    FREQ = E4 / (2 ** (4 - x))
    print("%.2f" % FREQ + " Hz")
elif NOTE[0] == "F":
    x = int(NOTE[1:])
    FREQ = F4 / (2 ** (4 - x))
    print("%.2f" % FREQ + " Hz")
elif NOTE[0] == "G":
    x = int(NOTE[1:])
    FREQ = G4 / (2 ** (4 - x))
    print("%.2f" % FREQ + " Hz")
elif NOTE[0] == "A":
    x = int(NOTE[1:])
    FREQ = A4 / (2 ** (4 - x))
    print("%.2f" % FREQ + " Hz")
elif NOTE[0] == "B":
    x = int(NOTE[1:])
    FREQ = B4 / (2 ** (4 -x))
    print("%.2f" % FREQ + " Hz")
else:
    print("Wrong input! The input should be one of C0 to C8.")

