my_list = [1, 2, 3, 3, 4, 5, 1]

my_list = set(my_list)
my_list = list(my_list)

# 1, 2, 3, 4, 5
print(my_list)

# <class 'list'>
print(type(my_list))
my_list.pop(-1)
# 1, 2, 3, 4
print(my_list)
