my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# # sets are useful for comparisons
# # return the items that are not common:
# print(my_set.difference(your_set))

# # remove element from set if member
# print(my_set.discard(5)) # returns `None`
# print(my_set)

# # remove all elements in this set from another set
# my_set.difference_update(your_set)
# print(my_set)

# # return the common items:
# my_set.intersection(your_set)

# # return True if nothing in common:
# my_set.isdisjoint(your_set)

# my_set.issubset(your_set)

# # 'superset' designates a set in relation to another set that it contains
# my_set.issuperset(your_set)

# # unite the sets (removing duplicates):
# print(my_set.union(your_set))
# # also: `print(my_set | your_set)`
