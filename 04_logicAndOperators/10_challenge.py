# check the password is at least 8 character and not contain white space

password = "abc defgh"

print(len(password) >= 8 and " " not in password)
