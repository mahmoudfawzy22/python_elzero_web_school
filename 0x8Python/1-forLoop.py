my_nums = [15, 81, 5, 17, 20, 21, 13]

index = 1
for i in my_nums:
    if not(i % 5):

        print(f"{index} ==> {i}")
        index += 1

else:
    print("All numbers are printed")
