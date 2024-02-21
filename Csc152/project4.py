import math #Math.pi is a requirement for the circle and ellipise so i had to add them.

def price(perimeter, area): # get the prices that I need all in one fucntion then individual ones 
    tax = 1.0635 # added the one so that way i get not just the tax but the total after tax is added
    sqft = 53.80 # price per square foot
    stone = 38.50 #price per foot of stone
    install = area * sqft #price calculation for the total square foot
    stoneWork = stone * perimeter #price calculation for the total perimeter
    total = (install+stoneWork)*tax #final price
    print("\nThe cost for this size pool is : $" + format(install, '.2f'))
    print("The cost of the stonework for this size pool is: $" + format(stoneWork, '.2f')) #information for customer
    print("The total cost of the pool will be: $"+format(total,'.2f'))
    
def getPoolType(): #determining what type of pool
    poolType = int(input("Would type of pool would you like? Circular, Elliptical, or Square?\nEnter 1 for Circular, 2 for Elliptical, 3 for Square: "))

    while poolType<1 or poolType>3 : 
        poolType = int(input("Invalid input. Please enter Circular, Elliptical or Square: ")) #input validation so only 1, 2 and 3 are taken

    if poolType == 1:
        circle()
        
    elif poolType == 2:
        ellipse()

    else:       #because only three options are avaialable i dont need to indicate that 3 is square because 1 and 2 are already assigned values
        square()
        
def circle(): 
    print("\nYou have selected circular.\n")
    d=int(input("How wide would you like your pool?(in feet): ")) #asking for diameter because it makes more sense than asking fro the radius
    r2 = d/2 #Making the diameter radius so that way i can use it in my caluclations
    area = math.pi*(r2**2)
    circum=(2*math.pi*r2)
    print("\nThe area of the pool is about:", format(area, '.2f'), "square ft") #printing information for the customers.
    print("The circumfrence of the pool is about:", format(circum, '.2f'), "ft")
    price(circum, area)#calling price and giving the appropriate values.

def ellipse():
    print("\nYou selected elliptical.\n")
    A = float(input("How wide would you like your pool? (in feet): "))#asking for diameter because it makes more sense than asking fro the radius
    B = float(input("How long would you like your pool? (in feet): "))
    a = A/2#Making the diameter radius so that way i can use it in my caluclations
    b = B/2
    area = (math.pi*a*b)
    numer = a**2 + b**2 #numerator 
    circum= (math.pi*2)* math.sqrt(numer/2) #circumfrence calulations
    print("\nThe area of the pool is about:", format(area, '.2f'), "square ft")
    print("The circumfrence of the pool is about:", format(circum, '.2f'), "ft")
    price(circum, area) #calling the price function and sending the values  needed to calulate the total price.
    
def square():
    print("\nYou selected square.\n")
    side = int(input("How wide would u like your pool? (in feet): "))
    perimeter = 4*side
    area= side**2
    print("\nThe area of the pool is about:", format(area, '.2f'), "square ft") #calculates total area
    print("The Perimeter of the pool is about:", format(perimeter, '.2f'), "ft") #caluclates total perimeter
    price(perimeter, area) #sends the calculations to price for customer

def main():
    print("Welcome to the virtual pool builder!") #I added an introduction just for presentation and general information
    print("Here you can build your own custom pool and Get an estimate on price!")
    print("Each foot of stone work will cost $38.50.")
    print("Installation will cost $53.80 per square foot.")
    print("Estimates may be rounded up or down to the nearest hundreth.\nThe total price is a relflection of actual total resorce costs before rounding.")
    print("in Connecticut sales tax is 6.35%")
    print("Lets get Started!\n")
    getPoolType() #starts the process of making a pool.
    
main()#initial function call.
