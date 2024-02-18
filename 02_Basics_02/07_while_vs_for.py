my_list = [1,2,3]
for item in my_list:
    print(item)

i = 0 # create variable (and halt it) for while loop
while i < len(my_list):
    print(my_list[i])
    i += 1

# Common while loop uses 'while True' and `break`
    
while True:
    input('say something: ')
    break

while True:
    response = input("say something: ")
    if response == 'bye':
        break
    
