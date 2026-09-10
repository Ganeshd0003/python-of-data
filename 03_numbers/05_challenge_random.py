import random

# Generate random number from 1 to 100 and check the output is even or not

num = random.randint(1, 100)

print(num)

if num % 2 == 0:
    print("Yes it is Even")
else:
    print("it is Odd")
