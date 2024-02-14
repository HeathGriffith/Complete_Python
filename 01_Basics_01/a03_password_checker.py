username = input("Username: ")
password = input("Password: ")

print(f'{username}, your password ' + len(password) * '*' + ' is '  + str(len(password)) + ' characters long.')

# guess at instructor's method:
hidden_pw = len(password) * '*'
pw_length = str(len(password)) # notice string conversion is superfluous
print(f'{username}, your password {hidden_pw} is {pw_length} characters long.')

# instructor:
# password_length = len(password)
# hidden_password = '*' * password_length
