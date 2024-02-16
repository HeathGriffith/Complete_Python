is_magician = True
is_expert = False

# check if both magician and expert: "you're a master"
if is_magician and is_expert:
    print("you're a master")

# check if magician and not expert: "you'll get there"
if not is_expert and is_magician:
    print("you'll get there")
     
# check if not magician: "You need magic."