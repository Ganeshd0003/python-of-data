# any , all


# website want any one from this
email = ""
mobile = "+91-123456789"
username = "ganesh"

print(any([email, mobile, username]))

# website want any two form this

print(bool(email)+bool(mobile)+bool(username) >= 2)

# website want all
print(all([email, mobile, username]))
