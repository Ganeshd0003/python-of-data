# search methods like : find() finds and Reults the postion number
#                       startsswith() find ends with text or char or number and Result True or False
#                       endswith() find ends with text or char or number and Result True or False
#                       in() find ends with text or char or number and Result True or False

date = "2026-Feb-19"

print(date.startswith("2026"))
print(date.startswith("2002"))

print(date.endswith("19"))

print("Feb" in date)
print("March" in date)
print("2026" in date)
print("2026 " in date)

print("\n"*3)

# Use Case startswith()
mobile_no = "+91-123457890"
print(mobile_no.startswith("+91"))

# Use Case endswith()
email = "ganesh@gmail.com"
print(email.endswith("gmail.com"))


# =====================================================
# Use Case find()
phone = "+91-12345678"
phone2 = "0091-12345678"
phone3 = "0-12345678"

# so we want a phone number without coutry code
print(phone[4:])  # this is static way and ineffecient
print(phone2[5:])  # this is static way and ineffecient

# best approch is dynamic with find()
print()
print(phone[phone.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])
