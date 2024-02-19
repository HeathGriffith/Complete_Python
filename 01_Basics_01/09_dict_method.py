# create dictionary
user = {
    'basket': [1, 2, 3],
    'greet': 'hello'   
}

# Typical way to access a value in dictionary: `dict[key]`
# to avoid error when key doesn't exit, use .get, which returns `None` 
# can specify default value to return for nonexistenet value
# print(user.get('age', 40))

# # a less common way to create a dict
# user2 = dict(name='Heath')
# print(user2)

# as in lists and strings, keyword `in` can be used for dictionaries
# print('basket' in user)
# print('hello' in user) # False because not a key

# method to only check keys explicity or to check values
# print('age' in user.keys()) # or .values()

# method to grab entire item: `items()`
# print(user.items())

# `.clear()` to return nothing, an empty dict
# `.copy()`
# user3 = user.copy()
# print(user.clear())
# print(user3)

# # `.pop(argument)` to remove key and return value
# user2 = {"name": "Emily", "age": 30}
# age = user2.pop('age')
# print(age)
# print(user2) 


# # `.update()` to add or update key-value pairs
# user3 = {"name": "John", "age": 25}
# user3.update({'greet': 'hello'}) 
# user3.update({'age': 30})  
# print(user3)  



