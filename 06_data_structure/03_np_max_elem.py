import numpy as np

arr = np.array([1, 3, 5, 64, 2, 0])

max = arr[0]

for i in arr:
    if i > max:
        max = i

print(f"Biggest elemnt in array is : {max}")