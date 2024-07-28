num = int(input("Enter the number large than zero  "))
ctr = num
if num == 0:
    print("The number 0 is not large than number 0")
else:
    num -=1
    while num > 0:

        if num == 6:
            num -=1 
            continue

        else:
            print(num)
            num -=1
            
    else:
        ctr = ctr - 2 if  ctr > 6 else ctr - 1
        print(f"{ctr} Numbers Printed Successfully.")
