emails = [
    "ganesh@.com",
    "baraa@.com",
    "drop table users;",
    "maria@.com"
]

for email in emails:

    if ';' in email:
        print("Sql Injection : Hacker attack")
        break
    print(f"Prcessing Email : {email}")
