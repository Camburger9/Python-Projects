number=int(input("Pick a number that is a multiple of 5 between 1 and 100: "))
if number %5==0 and 0<number<100:
    print("Your number is valid.")
else:
    print("Your number is invalid.")
