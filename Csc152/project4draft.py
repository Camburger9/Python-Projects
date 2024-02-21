import math

def price(circum, area):
    print("/nThe cost for this size pool is $" + format(area, '.2f')
    print("The cost of the stonework for this size pool is $", format(Circum, sep=(""))

def getPoolType():
    poolType = int(input("Would type of pool would you like? Circular, Elliptical, or Square?\nEnter 1 for Circular, 2 for Elliptical, 3 for Square: "))

    stone = 38.50
    sqft = 53.80
    tax = 1.0635
    
    while poolType<1 or poolType>3 : 
        poolType = int(input("Invalid input. Please enter Circular, Elliptical or Square: "))

    if poolType == 2:
        ellipse(stone, sqft, tax)

    elif poolType == 1:
        circle(stone, sqft, tax)

    else:
        square(stone, sqft, tax)
        
def circle(stone, sqft):
    print("You have selected circular.")
    r = int(input("How wide would you like your pool?: "))
    circum = math.pi*(r**2)
    area=(2*math.pi*r)
    print("The area of the pool is about:", format(area, '.2f'), "square ft")
    print("The circumfrence of the pool is about:", format(circum, '.2f'), "ft")
    install = sqft*area
    stoneWork = stone*circum
    price(Stonework, install)

def ellipse(stone, sqft):
    print("\nYou selected elliptical.")
    d = float(input("How wide would you like your pool?: "))
    b = float(input("How long would you like your pool?: "))
    a = d/2
    area = (math.pi*a*b)
    sqrt = a**2 + b**2
    circum= (math.pi*2)* math.sqrt(sqrt/2)
    print("The area of the pool is about:", format(area, '.2f'), "square ft")
    print("The circumfrence of the pool is about:", format(circum, '.2f'), "ft")
    install = sqft*area
    stoneWork = stone*circum
    price(stoneWork, install)
    
def square(stone, sqft, tax):
    print("You selected square.")

def main():
    print("Welcome to the virtual pool builder!")
    print("Here you can build your own custom pool and Get an estimate on price!")
    print("Each foot of stone work will cost $38.50.")
    print("Installation will cost $53.80 per square foot.")
    print("Estimates may be rounded up or down to the nearest hundreth.\nThe total price is a relflection of actual total resorce costs before rounding.")
    print("in Connecticut sales tax is 6.35%")
    print("Lets get Started!\n")
    getPoolType()
    
main()

