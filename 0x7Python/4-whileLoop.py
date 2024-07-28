my_friends = []
max_size = 4

index = 0

while index < max_size:
    name_friend = input("Enter the name of your friends").strip()

    if name_friend.isupper():
        print("Invalid Name")

    elif name_friend.islower():

        name_friend.capitalize()

        my_friends.append(name_friend)
        index += 1

        print(f"Friend {name_friend} Added => 1st Letter Become Capital")
    elif name_friend[0].isupper():

        my_friends.append(name_friend)
        index += 1

        print(f"Friend {name_friend} Add")
     
    print(f"There are {max_size - index} place to add another friend\n")

print(my_friends)   
