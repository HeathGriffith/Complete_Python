# Filter out all the numbers from mixed_list and create a new list called numbers_list.
# Filter out all the strings from mixed_list and create a new list called strings_list.
# For each number in numbers_list, multiply it by 2.
# For each string in strings_list, concatenate it with itself (e.g., 'a' becomes 'aa').
# Print both modified lists.

mixed_list = [1, 2, 'a', 'b', 3, 'c', 4, 'd', 'e', 5, 'f']

numbers_list = []
strings_list = []

for item in mixed_list:
    if type(item) == int:
        numbers_list.append(item * 2)
    else: strings_list.append(item * 2)

print(numbers_list)
print(strings_list)

