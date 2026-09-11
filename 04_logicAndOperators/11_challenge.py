# check if a user's email is not empty. contains @ and ends with '.com'

email = "ganesh@.com"

print(email != ""
      and "@" in email 
      and email.endswith(".com") 
      and " " not in email)
