#Display the picture where the 0 is going to be ' ',
#    and the 1 is going to be '*'. This will reveal an image!

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# # first try
# for row in picture:
#     for pixel in row:
#         if pixel == 0:
#             print(' ')
#         else:
#             print('*')

# # while-loop
# row = 0
# while row < len(picture):
#     GUI = []
#     for number in picture[row]:
#         if number == 0:
#             GUI.append(' ')
#         else:
#             GUI.append('*')
#     print(GUI)
#     row += 1

# # for-loop

# for row in picture:
#     GUI = []
#     for number in row:
#         if number == 0:
#             GUI.append(' ')
#         else:
#             GUI.append('*')
#     print(GUI)

# # *** fourth try: output string:

# for row in picture:
#     line = ''
#     for pixel in row:
#         if pixel == 0:
#             line += ' '
#         else:
#             line += '*'
#     print(line)

# # instructor solution
# for row in picture:
#     for pixel in row:
#         if (pixel == 1):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')

# instructor modified solution

fill = '*'
empty = ' '
for row in picture:
    for pixel in row:
        if pixel: # 1s are evaluated as true == 'if true . . .'
            print(fill, end='')
        else:
            print(empty, end='')
    print('')