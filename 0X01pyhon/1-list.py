friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
print(friends[0])

# "Osama" => Method Two
print(friends[-len(friends)])

# "Mahmoud" => Method One
print(friends[-1])

# "Mahmoud" => Method Two
print(friends[len(friends) - 1])
