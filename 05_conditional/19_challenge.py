# skip weekend in calander

days = ['sun', 'mon', 'tue', 'wed']

for d in days:
    if d == 'sun':
        print("Holdiday")
        continue
    print(f"Workday : {d}")
