# find dupliacte file name

files = ['report.csv', 'customer.csv', 'sales.csv', 'report.csv', 'sample.csv']
flag = 0
for i in range(len(files)):
    for j in range(i+1, len(files)):
        if files[i] == files[j]:
            flag = 1
            break

if flag == 0:
    print("Not Duplicate")
else:
    print("Duplicate")