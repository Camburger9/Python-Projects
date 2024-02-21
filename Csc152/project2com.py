buns = 8 #setting required variables for later functions and then making them int values.
int(buns)
hotdogs = 10
int(hotdogs)
#asking how many people will be in attendance
peeps = int(input("How many people will attend this coockout?: "))
#Hot dogs per person
hdpp = int(input("How many hot dogs will each person Eat?: "))
#needed hotdogs to purchase
nhdtp = peeps * hdpp
#Tells how many hotdogs you need to buy.
print(nhdtp, "hot dogs and buns are needed")
#we need to find the remainder of packs are needed so that if there is a remainder we can know to buy one more pack.
hdPacks = nhdtp%hotdogs
if(hdPacks > 0):
    print("You will need to buy", (nhdtp//hotdogs + 1), "packs of Hotdogs.") #adds the extra package if needed
    print("You will have", 10*(nhdtp//hotdogs+1)-nhdtp, "hotdogs left")#left overs
else:
    print("You will need to buy", (nhdtp//hotdogs), "packs of Hotdogs.")# if no extra packages are needed
bunPacks = nhdtp%buns
if (bunPacks > 0):
    print("you will need to buy", (nhdtp//buns+1), "packs of buns.")#adds the extra package if needed
    print("You will have", 8*(nhdtp//buns+1)-nhdtp, "buns left.")#left overs
else:
    print("You will need to buy", (nhdtp//buns), "packs of buns.")# if no extra packages are needed
