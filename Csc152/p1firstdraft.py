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
print('Your transaction fees are: $', format(fees, "0.2f"), sep='')
firstTransTotal = fees + priceForStocks
print("Payment due: $", format(firstTransTotal, "0.2f"), sep='')
#now im going to do the Math for 2 months later.
print('Two months later...')
#updating The price per share.
secondStockPrice = 42.75
secondPriceForStocks = secondStockPrice * totalStocks
#printing the total amount of money the stocks sell for.
print("Total value of shares is: $", format(secondPriceForStocks, "0.2f"), sep='')
fees2 = transFee * secondPriceForStocks
print('Your transaction fees are: $', format(fees2, "0.2f"), sep='')
#we subtract the fees this time because theyre being taken out of her total not added like when she was paying them.
secondTransTotal = secondPriceForStocks - fees2
print("You Made: $", format(secondTransTotal, "0.2f"), sep='')
profit = secondTransTotal - firstTransTotal
print("Your profits are: $", format(profit, "0.2f"), sep='')
#thats the job done. All requested inormation is there and more.
