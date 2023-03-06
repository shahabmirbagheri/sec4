#
age1 = input("age1 : ")
age2 = input("age2 : ")
age3 = input("age3 : ")
dict = {"ali": age1 ,"reza": age2 ,"mina": age3 }
if dict["ali"] > dict["reza"] :
    if dict["ali"] > dict["mina"] :
        print("ali")
if dict["reza"] > dict["ali"] :
    if dict["reza"] > dict["mina"] :
        print("reza")
if dict["mina"] > dict["ali"] :
    if dict["mina"] > dict["reza"] :
        print("mina")
else:
    print("ali")
    print("reza")
    print("mina")





