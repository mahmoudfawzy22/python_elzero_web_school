def reverse_string(my_string):
    for i in range(len(my_string) - 1, -1, -1):
        yield my_string[i]

# Reverse The String
for c in reverse_string("Elzero"):
    print(c)

