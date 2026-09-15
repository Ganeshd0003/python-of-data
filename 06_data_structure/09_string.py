import string

a = list(string.ascii_uppercase[:10])
print(a)

print(a)

# append() → adds an element at the end of the list
a.append("K")
print(a)

# insert(index, value) → adds an element at the specified index
a.insert(0, "Z")
print(a)

# pop() → removes (default) the last element from the list
a.pop()
print(a)

# remove(value) → searches for the value and removes its first occurrence
a.remove("A")
print(a)

# pop(index) → removes the element at the specified index
a.pop(0)
print(a)
