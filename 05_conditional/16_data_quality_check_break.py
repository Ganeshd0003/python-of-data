name = ["Ganesh", "Rohit", "        ", "Pranit"]

for n in name:

    if n.strip() == "":
        print("Empty value detected")
        break

    print(f"Name = {n}")
