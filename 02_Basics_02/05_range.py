# print(range(100)) # gives range object 
# print(range(0,100)) # same

# for number in range(1, 100):
#     print(number)

# for _ in range(0, 10): # '_' variable indicates we don't care what the number is
#     print("Hi")

# for _ in range(0, 10, 2): # third parameter is a step over with default 1
#     print(_)

# for _ in range(10, 0, -1): # go in reverse
#     print(_)

# for _ in range(10, 0, -2): # loop five times
#     print(list(range(10))) # convert range (literable item) into list

# for char in enumerate('Hello'): # enumerate takes iterable object
#     # gives index and item of index
#     print(char)
# # But this is less readable, and each tuple would need to be 
#     # unpacked to access elements; 

# # Hence, correct approach is usually to unpack upfront:
# for i, char in enumerate('Hello'):
#     print(i, char)

# for i, number in enumerate(list(range(100))):
#     if number == 50:
#         print(f'the index of 50 is {i}')