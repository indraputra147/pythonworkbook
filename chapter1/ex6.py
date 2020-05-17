#Excercise 6: Tax and Tip
MealCost = float(input("Input the cost of the meal: "))
Tax = 0.1 * MealCost
Tip = 0.18 * MealCost
GrandTotal = MealCost + Tax + Tip
print("Total of the price is Rp.%.2f" % GrandTotal)
