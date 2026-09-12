# remove white spaces, keep all in lower, and format must be csv

files = ["  Report.csv", "datA.csv", "TEXt.txt"]

clean = []

for f in files:
    clean.append(f.strip().lower().replace("txt", "csv"))

print(clean)
