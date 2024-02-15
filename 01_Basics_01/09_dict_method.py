user = {
    'basket': [1, 2, 3],
    'greet': 'hello'   
}

# to avoid error, use .get; 
# can use default value to return for nonexistenet value
# print(user.get('age', 40))

# # a less common way to create a dict
# user2 = dict(name='Heath')
# print(user2)

# as in lists and strings, keyword `in` can be used for dictionaries
# print('basket' in user)
# print('size' in user)

# method to only check keys or only values
# print('age' in user.keys()) # or .values()

# method to grab entire item: `items()`
# print(user.items())

# `.clear()` to return nothing, an empty dict
# `.copy()`
# user3 = user.copy()
# print(user.clear())
# print(user3)

# `.pop()` to remove key and return value
# print(user.pop('age'))
# print(user)

# `.update()` will create new key item if doesn't exist
print(user.update({'greet': 'goodbye'}))
print(user.update({'ages': 55}))
print(user)


