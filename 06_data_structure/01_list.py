# this is empty list
empty = []
print(type(empty), empty)

# this is list of numbers
lst = [2, 4, 23]
print(type(lst), lst)

# mixed list with diff diff data types
mixed = [1, 'Mango', 7.3, True]
print(type(mixed), mixed)

# this is list of strings
fruits = ['Apple', 'Banana', 'Cherry']
print(type(fruits), fruits)

# printing address of list, elements
print(id(fruits))  # in decimal

print(hex(id(fruits)))  # in hexadecimal)

print(id(fruits[0]))

print(hex(id(fruits[0])))
