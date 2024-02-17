# for item in (1,2,3,4,5):
#     print(item)
# print(item) # notice 'item' here is set as the final element

# # nested loop
# for number in (6,7,8,9,10):
#     for letter in ['a','b','c']:
#         print(number, letter)

# an iterable is a collection that can be iterated over: 
        # string, list, dictionary, tuple, set
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

# # print keys
# for item in user:
#     print(item)

# three methods to loop over keys and values
    # .items() >> key-value pair in tuple
    # .values() >> gives values
    # .keys() >> explicit about getting keys

# # to print keys and values separately
# # longform:
# for element in user.items():
#     key, value = element
#     print(key, value)
# # shortform:
# for key, value in user.items():
#     print(key, value)

for a, b in user.items():
    print(b,a)