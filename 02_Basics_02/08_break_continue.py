# `break` breaks out of loop, 
# `continue` continues to top of enclosing loop, and 
# `pass` is a placeholder, rarely used

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for item in my_list:
    if item % 2 == 0:  
        continue      # skip printing even number and continue next iteration
    print(item)  


my_list_2 = [1, 2, 3, 4, 5]

i = 0
while i < len(my_list_2):
    if my_list_2[i] % 2 == 0:  
        i += 1
        continue
    print(my_list[i])
    i += 1
