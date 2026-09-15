letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

combine = letters + numbers
print(combine)

print(letters * 2)

combine2 = [[letters], [numbers]]
print(combine2)

letters.extend(numbers)
print(letters)

