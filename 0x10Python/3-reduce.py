from functools import reduce

nums = [2, 4, 6, 2]

sum = reduce(lambda num, num2: num * num2, nums)

print(sum)
