some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# check for duplicates

# Approach 1 fail: isolated non-duplicates, unuseable
# set_some_list = set(some_list)

# for letter in set_some_list:
#     if letter in some_list:
#         some_list.remove(letter)
# print(some_list)

# *** Try two

unique_values = []
for letter in some_list:
    if letter not in unique_values:
        unique_values.append(letter)

for letter in unique_values:
    some_list.remove(letter)

print(some_list)

# instructor solution:
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)
