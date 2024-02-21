def main():
    inFile = open("studentInfo.txt", 'w')
    x=0
    
    for x in range(3):
        lastName = input("Enter last name: ")
        firstName = input("Enter first name: ")
        studentID = input("Enter ID: ")
        credit = input("How many credits have you earned so far?: ") 
        inFile = open("studentInfo.txt", 'a')
        inFile.write("Name: " + firstName + " " + lastName)
        inFile.write("\nStudentID: " + studentID)
        inFile.write("\nCredits earned: "+credit)
        inFile.write("\n\n")
        x+1
        
    inFile.close()
    print("Done! Data is saved in file: studentInfo.txt")

main()
