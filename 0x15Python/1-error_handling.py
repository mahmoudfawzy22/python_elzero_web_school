NUM = input("Add Your Number ")

if len(NUM) > 1 :
    raise IndexError("Only  One Character Allowed")

elif NUM == 0 :
    raise ValueError("Number Must Be Larger Than 0")

elif NUM.isalpha() :
    raise Exception("Only Numbers Allowed")

else:
    print(16 * '=')
    print("The Number Is ", NUM)
    print(16 * '=')

