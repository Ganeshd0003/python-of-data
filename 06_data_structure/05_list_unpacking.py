person = ['Ganesh', 25, "Data Engineer", "India"]

# name = person[0]
# age = person[1]
# role = person[2]
# country = person[3]

# Insted of doing manually we can do same thing effeciently with "list unpacking"

name, age, role, country = person

print(name, age, role, country)

# ================================================================================
# "*" Asters
# Suppose we want only name and country
# Only One Asters one time

person2 = ['Maria', 25, 'Data Analyst', 'USA', 'Female',
           50000, 'New York', 5, 'Python', 'SQL', 'Full-time']


# Using * to collect the remaining elements
name2, *details, jobtype2 = person2

print(name2, jobtype2)


# Using _ to ignore unwanted elements
# *_ collects and ignores all remaining elements (_ not store anything it is skip that values)
name3, _, _, country3, *details, jobtype3 = person2

print(name3, country3, jobtype3)
