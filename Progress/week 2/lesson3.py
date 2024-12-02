#conditional statements
username="user"
password="password"

is_correct_username=username=="user"
is_correct_password=password=="password"

is_authenticated= is_correct_username and is_correct_password
if is_authenticated:
    print('Welcome to our Database')
else:
    print("Unknown User trying to access the database")


