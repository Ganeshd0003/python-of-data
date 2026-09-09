phone = "+1 (123) 456-789"

phone = phone.replace("+", "").replace(" ",
                                       "").replace("(", "").replace(")", "").replace("-", "")

print(phone)
