import random #random Required for random Ints
def main():
    inFile = open("ranNums",'w') # file name and making openeing the file an ez varaible
    
    mylist = [] #name of my list
    total=0 #varible to calculate Average
    for x in range(1,21):
        n = random.randint(1,100) #random number
        mylist.append(n) #adds the number to the list so i can find the smallest and the largest
        inFile.write(str(n))#cant write ints or lists to files. sends the numbers seperate 
        inFile.write("\n")#next line for formating
        total+=n #running sum for average
    mylist.sort() # sorts from lowest to highest
    inFile.close() #closes file
        
    read(mylist, total)#sends My 2 values to the read function
    
def read(mylist,total):
    inFile = open("ranNums", 'r')
    print(inFile.read()) #read works better in the way i wrote my code.
    print("The smallest number is:", mylist[0])#first number is the lowest after sorting
    print("The largest number is:", mylist[-1])#last number is highest after sorting
    print("The average of the numbers is:", format(total/20, '.2f'))    
    inFile.close()
    
main()
