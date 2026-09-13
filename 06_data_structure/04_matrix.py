# 1) 1D matrix
a = [1, 2, 3]

# 2) 2D matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix)


# 3) 2D matrix
mixed_matrix = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    ['Apple', 'Banana', 'Cherry']
]
print(mixed_matrix)


# Indexing
# print banana
print(mixed_matrix[2][1])

# print banana with -ve index
print(mixed_matrix[-1][-2])


# Slicing
print(mixed_matrix[:2])


# 3D matrix

t = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
]

print(t[0][1][1])
