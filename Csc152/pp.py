hamburgers = float(input("How many hamburgers would you like?: "))
fries=float(input("How many orders of fries would you like?: "))
drinks=float(input("How many drinks would you like?: "))
burgerCost=(hamburgers*2.00)
fryCost=(fries*1.50)
drinkCost=(drinks*1.00)
totalCost=(burgerCost+fryCost+drinkCost)
print("Your total will be $", format(totalCost, "0.2f"), sep='')

