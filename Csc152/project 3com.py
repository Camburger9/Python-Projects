x=0 # needs to be zero because it is the value that is measured to determine how many times we need to loop
threeYearTotal=0 #I needed a value that would be unchangeing starting at zero to measure the rain fall
for x in range(3): #loops 3 times once per measured year
    print("\nYear "+str(x+1)+":")#starting a new line, to start off a fresh for each year
    y=0 #y is the variable that measures months that starts at 0 and ends at 12
    total=0 #total rain fall each year needs to be reset to print on a year by year basis
    while y < 12: #loop to get all 12 months
        rainfall=float(input("Enter how much rain fell during month " +str(y+1)+":"))
        while (rainfall < 0):#input validation
            print("invalid entry please try again")
            rainfall=float(input("Enter how much rain fell during month "+str(y+1)+":"))#getting a valid value if one wasnt entered
        total+=rainfall#consoidation of inputs
        y+=1# adds to why so it knows to loop one less time after each loop
    average=total/12
    threeYearTotal+=total
    print("Total rainfall for year is:", format(total,".2f"))#printing the total and average
    print("The average rainfall this year is:", format(average,".2f"))
x+=1
print("\nTotal rain fall for three years:", threeYearTotal) #prints total and average for all three years
print("The average for all three years is:", format(threeYearTotal/36,".2f"))
