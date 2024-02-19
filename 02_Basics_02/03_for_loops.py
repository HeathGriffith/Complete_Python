# Iteration

# # Basic Iteration with a Tuple
# for item in (1, 2, 3, 4, 5):
#     print(item)
# # Note: 'item' retains the value of the last element outside the loop.
# print(item)  # Output: 5

# # Nested Loop Example
# # Demonstrates iterating over combinations of numbers and letters.
# for number in (6, 7, 8, 9, 10):
#     for letter in ['a', 'b', 'c']:
#         print(number, letter)

# # An iterable is any object that can be looped over, including:
# # Strings, Lists, Dictionaries, Tuples, Sets


# # Looping Through a Dictionary

# # Sample dictionary:
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

# # Basic Iteration: Printing All Keys
# # Direct iteration over a dictionary defaults to iterating over its keys.
# for key in user:
#     print(key)  # Outputs: 'name', 'age', 'can_swim'

# Methods for Iterating Over Dictionaries

# .items(): For the purpose of iteration or when you need to view the dictionary's contents, 
    # .items() presents each key-value pair as a tuple. This makes it convenient for iteration, 
        # unpacking, and other operations where you might want to work with keys and values simultaneously.
# Shortform Directly Unpacks the Tuples Returned by .items()
for key, value in user.items():
    print(key, value)  # Prints each key followed by its corresponding value

# Longform Explicitly Unpacks the Tuple Into Variables Inside the Loop
for element in user.items(): #first retrieve tuple 'element'
    key, value = element  # unpack element into variables (first item to key, second, to value)
    print(key, value)  

# (2) .values() Method: Iterating Over Values
# To iterate over just the values of the dictionary:
for value in user.values():
    print(value)  # Outputs each value in the dictionary: 'Golem', 5006, False

# (3) .keys() Method: Explicit Iteration Over Keys
# While iterating directly over the dictionary also iterates over keys, .keys() makes this explicit.
for key in user.keys():
    print(key)  # Outputs each key in the dictionary: 'name', 'age', 'can_swim'

# For demonstration, keys and values can be swapped directly in the print statement.
for key, value in user.items():
    print(value, key)  # Swaps the position of key and value in the output
