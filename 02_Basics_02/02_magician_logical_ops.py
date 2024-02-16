is_magician = False
is_expert = True

# check if both magician and expert: "you're a master"
if is_magician and is_expert:
    print("you're a master")

# check if magician and not expert: "you'll get there"
elif not is_expert and is_magician:
    print("you'll get there")

else:
    print("you need magic")