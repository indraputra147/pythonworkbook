#Exercise 55: Wavelength of Visible Light

"""
The program reads a wavelength from the user and report its color
"""

WAVE = float(input("Enter a wavelength in nanometers: "))

if WAVE >= 380 and WAVE < 450:
    print("Violet")
elif WAVE >= 450 and WAVE < 495:
    print("Blue")
elif WAVE >= 495 and WAVE < 570:
    print("Green")
elif WAVE >= 570 and WAVE < 590:
    print("Yellow")
elif WAVE >= 590 and WAVE < 620:
    print("Orange")
elif WAVE >= 620 and WAVE < 750:
    print("Red")
else:
    print("Out of range!")

