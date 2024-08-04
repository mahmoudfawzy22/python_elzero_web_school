from random import randint

while(True):
    x = randint(2, 10)
    if x % 2 == 0:
        break

while(True):
    odd = randint(2, 10)
    if odd % 2 == 0:
        break

print(f"Random Number Between 10 And 50 => {randint(10, 50)}")

print(f"Random Even Number Between 2 And 10 => {x}")

print(f"Random Odd Number Between 1 And 9 =>{odd}")


