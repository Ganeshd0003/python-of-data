# 1) To generate daily report

years = [2025, 2026]
months = ['Jan', 'Mar']
days = range(1, 32)

for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")


print("\n"*5)

# 2) Generate SQL scripts to check NULL values in specified tables and columns
#    This uses a metadata-driven approach: table and column names are maintained

tables = ['customers', 'sales', 'orders', 'products']

columns = ['customer_id', 'create_date']

# Generate a NULL-check query for each table-column combination
for t in tables:
    for c in columns:
        print(f"SELECT COUNT(1) FROM {t} WHERE {c} IS NULL;")
