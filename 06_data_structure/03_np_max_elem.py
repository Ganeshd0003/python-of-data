import math
import numpy as np

# Manual Approach to find biggest element
arr = np.array([1, 3, 5, 64, 2, 0])

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print(f"Biggest element in array is : {largest}")


print()


# Built-in approach

no = np.random.randint(1, 1000, 10)
nos = []
for i in no:
    nos.append(i)

print(no)

arr2 = np.array(nos)
print(f"Biggest element in array is : {max(arr2)}")
