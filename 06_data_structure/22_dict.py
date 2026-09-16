# Values can be duplicated
dictt = {'a': 1, 'b': 1, 'c': 1}
print(dictt)

# Keys must be unique.
# If a key is repeated, the last value overwrites the previous value.
dicttt = {'a': 10, 'a': 'something', 'a': 'nothing'}
print(dicttt)

user = {'name': 'Ganesh', 'age': 20, 'role': 'data engineer'}
print(user)
print(user.get("name"))

print("age" in user)

print()


for u in user:
    print(u, user[u])

print()

for key, value in user.items():
    print(key, value)
