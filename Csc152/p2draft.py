buns = 8
int(buns)
hotdogs = 10
int(hotdogs)
#asking how many people will be in attendance
peeps = int(input("How many people will attend this coockout?: "))
#Hot dogs per person
hdpp = int(input("How many hot dogs will each person Eat?: "))
#needed hotdogs to purchase
nhdtp = peeps * hdpp
print(nhdtp, "hot dogs and buns are needed")
hdPacks = nhdtp%hotdogs
if(hdPacks > 0):
    print("You will need to buy", (nhdtp//hotdogs + 1), "packs of Hotdogs.")
    print("You will have", 10*(nhdtp//hotdogs+1)-nhdtp, "hotdogs left")
else:
    print("You will need to buy", (nhdtp//hotdogs), "packs of Hotdogs.")
bunPacks = nhdtp%buns
if (bunPacks > 0):
    print("you will need to buy", (nhdtp//buns+1), "packs of buns.")
    print("You will have", 8*(nhdtp//buns+1)-nhdtp, "buns left.")
else:
    print("You will need to buy", (nhdtp//buns), "packs of buns.")
