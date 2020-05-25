#Exercise 40: Sound Levels

"""
The program reads a sound level in decibels from the user
display a message containng the noise
"""

Sound = float(input("Enter a sound level in decibel: "))

if Sound < 40:
    print("Quieter than Quiet room!")
elif Sound == 40:
    print("Quiet Room")
elif Sound > 40 and Sound < 70:
    print("Between Quiet Room and Alarm Clock")
elif Sound == 70:
    print("Alarm Clock")
elif Sound > 70 and Sound < 106:
    print("Betweem Alarm Clock and Gas Lawnmower")
elif Sound == 106:
    print("Gas Lawnmower")
elif Sound > 106 and Sound < 130:
    print("Between Gas Lawnmower and Jackhammer")
elif Sound == 130:
    print("Jackhammer")
elif Sound > 130:
    print("Louder than Jackhammer!")
else:
    print("Wrong Input!")
