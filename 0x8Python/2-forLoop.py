# skipNumbers = [6, 8, 12]

# for i in range(1, 21):
#     if i not in skipNumbers:
#         print(str(i).zfill(2))
# else:
#     print("All numbers printed")

for i in range(1, 21):
    if i == 8 or i == 6 or i == 12:
        continue

    else:
        print(str(i).zfill(2))

else:
    print("All numbers printed")
