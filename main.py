# Function to validate a password
def is_valid_password(password):
    # Check if the password is at least five characters long
    if len(password) < 5:
        return False

    # Check if the password contains the symbol "&"
    if '&' not in password:
        return False

    # Check if the password contains at least one uppercase and one lowercase letter
    has_lowercase = False
    has_uppercase = False
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
    if not (has_lowercase and has_uppercase):
        return False

    return True


# Input a password from the user
password = input("Enter a password: ")

# Check if the password is valid
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password does not meet the requirements.")
