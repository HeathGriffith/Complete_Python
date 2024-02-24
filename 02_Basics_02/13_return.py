# # functions should do one thing well and return something
# def sum(num1, num2):
#     return num1 + num2

# total = sum(10,5) 
# print(sum(10,total))

# # also: `print(sum(10,sum(10,15)))`

def sum(num3, num4):
    def another_func(n3, n4):
        return n3 + n4
    return another_func(num3, num4)

total = sum(10,20)
print(total)

