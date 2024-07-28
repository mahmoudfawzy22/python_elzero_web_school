friends = ("Osama", "Ahmed", "Sayed")

friends_list = list(friends)

friends_list[0] = "Elzero"

friends = tuple(friends_list)

print(friends)

print(type(friends))

print(f"{len(friends)} elements in tuple")

