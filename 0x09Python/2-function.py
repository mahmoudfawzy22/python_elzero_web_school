def addition(*numbers):

    sum = 0

    for i in numbers:

        if i == 10:
            continue

        elif i == 5:
            sum -= 5

        else:
            sum += i

    return sum

print(addition(10, 20, 30, 10, 15))
print(addition(10, 20, 30, 10, 15, 5, 100))
