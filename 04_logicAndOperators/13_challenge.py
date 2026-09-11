# check if the user is either admin or a moderator, and either they are not banned or verified email

user_type = "admin"
is_not_banned = ['.fake', '.org']
verified_email = ".com"
email = "ganesh@123.com"


print(user_type in ['admin', 'moderator']
      and email.endswith(".com"))
