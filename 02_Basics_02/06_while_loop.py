# infinte loop
i = 0
while 0 < 50:
    print(i)
    # break out of while loop with `break`
    break

# break out of while loop without `break` by turning condition false
# loop 7 times
i = 0
while i < 7:
    print(i)
    i += 1
# while loops can include else blocks, which only run if condition is
    # false (loop finished) without `break` statement:
else:
    print("Finished!")