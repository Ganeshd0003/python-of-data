# allow access only if the user is logged in or they are guest but they must not banned

is_logged_in = True
is_guest = False
is_not_banned = False

print((is_logged_in or is_guest) and is_not_banned)
