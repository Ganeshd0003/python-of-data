my_set = {1, 2, 3}
print(my_set)

a = {1, 1, 1, 2, 3, 4, 5, 5}
print(a)

a.add(50)
print(a)

a.update({1,22})
print(a)

a.remove(1)
# print(a)
# a.remove(999) # if we execute this so it breaks code if the value if not present
# so we use discrad()

a.discard(9999)
print(a)