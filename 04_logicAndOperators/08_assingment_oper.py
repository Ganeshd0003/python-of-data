a = ['x', 'y', 'z']
b = ['x', 'y', 'z']

print(a == b)
print(a is b)


print()
c = ['x', 'y', 'z']
d = c

print(c == d)
print(c is d)


print()
e = 10
f = 10

print(e == f)
print(e is f)


print()
# use case : Make sure email is exits or not
email = None
print(email == None and email == "")
