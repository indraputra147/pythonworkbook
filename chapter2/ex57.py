#Exercise 57: Cell Phone Bill

"""
The program reads the number of minutes and text messages used in month
display base charge. additional minutes charge, additional text message charge, the 911 fee, tax and total bill amount
Only display the additional minute and text message charges if the user
incurred cost in these categories. in 2 desimal places
"""

MINUTE = int(input("Total minute of air time: "))
TEXT = int(input("Total Message: "))
BASE_CHARGE = 15.00
ADD_MINUTE = 0.25
ADD_TEXT = 0.15
SUPPORT = 0.44

print("BASE_CHARGE              = $%.2f" % BASE_CHARGE)
print("911 FEE                  = $%.2f" % SUPPORT)

if MINUTE <= 50:
    if TEXT <= 50:
        BILL = BASE_CHARGE + SUPPORT
        TAX = BILL * 0.05
        TOTAL = BILL + TAX
        print("TAX                      = $%.2f" % TAX)
    else:
        BILL = BASE_CHARGE + SUPPORT
        ATC = (TEXT - 50) * ADD_TEXT
        TAX = (BILL + ATC) * 0.05
        TOTAL = BILL + ATC + TAX
        print("ADDITIONAL TEXT CHARGE = $%.2f" % ATC)
        print("TAX                    = $%.2f" % TAX)
elif MINUTE > 50:
    if TEXT <= 50:
        BILL = BASE_CHARGE + SUPPORT
        AMC = (MINUTE - 50) * ADD_MINUTE
        TAX = (BILL + AMC) * 0.05
        TOTAL = BILL + AMC + TAX
        print("ADDITIONAL MINUTE CHARGE = $%.2f" % AMC)
        print("TAX                      = $%.2f" % TAX)
    else:
        BILL = BASE_CHARGE + SUPPORT
        AMC = (MINUTE - 50) * ADD_MINUTE
        ATC = (TEXT - 50) * ADD_TEXT
        TAX = (BILL + ATC + AMC) * 0.05
        TOTAL = BILL + AMC + ATC + TAX
        print("ADDITIONAL MINUTE CHARGE = $%.2f" % AMC)
        print("ADDITIONAL TEXT CHARGE   = $%.2f" % ATC)
        print("TAX                      = $%.2f" % TAX)
else:
    print("Wrong Input! Please Try Again")

print("TOTAL BILL AMOUNT        = $%.2f" % TOTAL)
