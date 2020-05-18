#Exercise 8: Widgets and Gizmos
"""
An online retailer sells two products:
widgets: 75 grams
Gizmos: 112 grams
"""
w = 75
g = 112

nw = int(input("Input the number of widget: "))
ng= int(input("Number of Gizmo: "))
tw = w * nw
tg = g * ng
total = tw + tg
print("The total weight is ", total)
