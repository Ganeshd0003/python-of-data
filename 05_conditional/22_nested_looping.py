for i in range(1, 5):
    for j in range(i+1, 5):
        print(f"({i} , {j})", end=" | ")


print()
for i in range(1, 5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            print(f"({i} , {j}, {k} )", end=" | ")


print("\n"*2)


# use case

color = ['Red', "Green", "Blue"]
size = ['Small', 'Meduim', 'Large']

for i in color:
    for j in size:
        print(f"Colur : {i} with Size : {j}")
