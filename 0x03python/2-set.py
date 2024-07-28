nums = {1, 2, 3}
letters = {"A", "B", "C"}

nums_letters = nums.union(letters)
print(nums_letters)

# {1, 2, 3, "A", "B", "C"}
nums_letters2 = nums | letters
print(nums_letters2)

# {1, 2, 3, "A", "B", "C"}
nums_letters3 = nums.copy()
nums_letters3.update(letters)
print(nums_letters2)
