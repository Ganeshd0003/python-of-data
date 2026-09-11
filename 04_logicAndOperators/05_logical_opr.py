# 3 < 5 and 3 > 1
# "and" have more priority than "or"
print(3 < 5 and 3 > 1)

print(3 < 5 or 3 > 1)

print(3 < 5 and 0 > 1)


# use case
username = "ganesh"
password = 12345

u = str(input("Enter username : "))
p = int(input("Enter password : "))

print(username == u and password == p)
