letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3]

comb = zip(letters, numbers)
print(comb)
print(list(comb))


# use cases
ids = [101, 102, 103]
names = ['Ganesh', 'Rohit', 'Pranit']

print(list(zip(ids, names)))
