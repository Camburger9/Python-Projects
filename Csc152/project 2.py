buns = 8
hotdogs = 10
(hotdogs)
peeps = int(input("How many people will attend this coockout?: "))
hdpp = int(input("How many hot dogs will each person Eat?: "))
nhdtp = peeps * hdpp
print(nhdtp, "hot dogs and buns are needed")
hdPacks = nhdtp%hotdogs
if(hdPacks > 0):
    print("You will need to buy", (nhdtp//hotdogs + 1) "packs of Hotdogs.")
else:
    print("You will need to buy", (nhdtp/hotdogs), "packs of Hotdogs.")
bunPacks = nhdtp%buns
if (bunpacks > 0)
    print("you will need to buy", (nhdtp//buns+1), "packs of buns.")
else:
    print("You will need to buy", (nhdtp/buns), "packs of buns.")
