import numpy as np

a = np.random.randint(1, 100, 12)

print("Array:", a)

# Min
print(f"Min : {np.min(a)}")

# Max
print(f"Max : {np.max(a)}")

# Sum
print(f"Sum : {np.sum(a)}")

# Length
print(f"Len : {len(a)}")

# Mean
print(f"Mean : {np.mean(a)}")

# Standard Deviation
print(f"Standard Deviation : {np.std(a)}")

# Product of all elements
print(f"Product : {np.prod(a)}")

# Sort
print(f"Sorted : {np.sort(a)}")

# Count elements satisfying a condition
print(f"Count > 50 : {np.count_nonzero(a > 50)}")

# Index of minimum element
print(f"Index of Min : {np.argmin(a)}")

# Index of maximum element
print(f"Index of Max : {np.argmax(a)}")

# Any - Is at least one element > 90?
print(f"Any > 90 : {np.any(a > 90)}")

# All - Are all elements > 0?
print(f"All > 0 : {np.all(a > 0)}")

# Analyse and check
print(f"8 in a : {8 in a}")
