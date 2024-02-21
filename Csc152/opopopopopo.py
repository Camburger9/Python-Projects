numFile=open("nums.txt",'r')

summ=0
lines=numFile.readline().rstrip()

while lines !="":
    nums=int(lines)
    print(nums)
    summ+=nums
    lines = numFile.readline().rstrip()

print("And the sum is:", summ)

numFile.close()
             
