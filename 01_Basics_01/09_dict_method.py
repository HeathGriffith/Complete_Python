# Define a dictionary
user = {"name": "John", "age": 25}

# Checking existence
print('age' in user)  # True - Checks if 'age' is a key
print(25 in user.values())  # True - Checks if 25 is a value

# Accessing elements
print(user['name'])  # "John" - Direct access, KeyError if not exists
# Using .get() avoids KeyError. Returns None if key not found, unless a default is provided.
print(user.get('age'))  # 25
print(user.get('height'))  # None, since 'height' is not a key and no default value is specified
print(user.get('height', 'Not Available'))  # 'Not Available' - Default value if key not found


# Adding and updating elements
user['location'] = 'New York'  # Adds a new key-value pair
user.update({'age': 30, 'greet': 'hello'})  # Updates 'age' and adds 'greet'

# Deleting elements
del user['location']  # Removes 'location' key
age = user.pop('age')  # Removes 'age' and returns its value

# Working with keys, values, and items
print(user.keys())  # dict_keys(['name', 'greet']) - View of keys
print(user.values())  # dict_values(['John', 'hello']) - View of values
print(user.items())  # dict_items([('name', 'John'), ('greet', 'hello')]) - View of items

# Copying a dictionary
user_copy = user.copy()  # Creates a shallow copy of the dictionary

# Clearing a dictionary
user.clear()  # Empties the dictionary

# Creating dictionaries
user2 = dict(name='Heath')  # Another way to create a dictionary



## Note Shallow copy explanation
# Template for user profiles
user_template = {
    "name": "",
    "age": 0,
    "preferences": {"theme": "light", "notifications": True}
}

# Creating a new user profile from the template
user1 = user_template.copy()
user2 = user_template.copy()

# Customizing each user
user1["name"] = "Alice"
user1["age"] = 24
user2["name"] = "Bob"
user2["age"] = 30

# At this point, user1 and user2 have their unique names and ages,
# but share the same preferences dictionary due to shallow copying.

# If you need to change a preference uniquely, make a copy of the preferences dictionary itself.
user1["preferences"] = user1["preferences"].copy()
user1["preferences"]["theme"] = "dark"

# Now user1's preferences have been customized without affecting user2 or the template.
print(user1["preferences"])  # Output: {'theme': 'dark', 'notifications': True}
print(user2["preferences"])  # Output: {'theme': 'light', 'notifications': True}


## Template for user profiles to demonstrate why .copy() was needed
user_template = {
    "name": "Template Name",
    "age": 0,
    "preferences": {"theme": "light", "notifications": True}
}

# Setting user1 and user2 to the template directly
user1 = user_template
user2 = user_template

# Attempting to customize user1
user1["name"] = "Alice"
user1["age"] = 24

# Now, user2 also sees these changes because user1 and user2 are the same object as user_template
print(user2)  # Output will show that user2's name is also "Alice" and age is 24
