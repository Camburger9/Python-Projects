#Here we have the price per share and total shares.
totalStocks = 200
firstStockPrice = 40
# I made these values floats so that they can multiply by decimals later on.
float(totalStocks)
float(firstStockPrice)
#these equations get me the values i need to multiply to get to the Stock prices before and after the fees.
priceForStocks = firstStockPrice * totalStocks
print('Your total before fees will be: $', priceForStocks, sep='')
transFee = .03
fees =  transFee * priceForStocks
firstTransTotal = fees + priceForStocks
print("Payment due: $", firstTransTotal, sep='')
#now im going to do the Math for 2 months later.
print('Two months later...')
secondStockPrice = 42.75
secondPriceForStocks = secondStockPrice * totalStocks
print("Total share value is: $", secondPriceForStocks, sep='')
fees2 = transFee * secondPriceForStocks
print(fees2)
secondTransTotal = secondPriceForStocks - fees2
print("You Made: $", secondTransTotal, sep='')
profit = secondTransTotal - firstTransTotal
print("Your profits are: $", format(profit, "0.2f") sep='')
