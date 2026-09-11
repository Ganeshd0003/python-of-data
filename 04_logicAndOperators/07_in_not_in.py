# in    not in    operator

x = "data"
print('a' in x)
print('z' in x)


print("G" not in "ganesh")

print(3 in [1, 2, 3, 4, 5])


print()
# Use case : security check to ensure domain is not banned
domain = "gmail.com"
banned_domain = ["fake.org", "zohomail.com", "mail.com"]

print(domain not in banned_domain)
