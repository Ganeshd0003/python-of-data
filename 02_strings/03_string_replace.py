# replace for string
stringg = """
Python is very easy langauge.
Python is very powerful.
My favourite langugae is python.
"""

print(stringg.replace("Python", "C"))
print(stringg)

# replace for numbers (single replace)
phone = "123-456-789"
phone = phone.replace("-", "")
print(phone)

# replace for numbers (multiple replace)
price = "$1,000"
price = price.replace("$", "*").replace(",", "")
print(price)
