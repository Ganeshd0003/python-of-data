# 1

names = ["Ganesh", "None", "Rhoit"]

for name in names:
    if name is None:
        print("Name is Missing")
        break
else:
    print("All names are avilable")


# 2

files = ["report.csv", "report2.pdf", "report3.csv"]

for file in files:
    if not file.endswith(".csv"):
        print(f"{file}")
        break
else:
    print("All files are csv")
