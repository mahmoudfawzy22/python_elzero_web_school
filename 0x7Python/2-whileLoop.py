friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

friendsLen = len(friends)
index, ctrP = 0, 0

while index < friendsLen:
    if(friends[index][0].isupper()):

        print(f"\"{friends[index]}\"")
        ctrP += 1

    index += 1

else:
    print(f"Friends Printed And Ignored Names Count Is {len(friends) - ctrP}")
