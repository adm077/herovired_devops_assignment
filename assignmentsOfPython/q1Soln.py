'''
Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 

●       Implement a Python function called check_password_strength that takes a password string as input.

●       The function should check the password against the following criteria:

○       Minimum length: The password should be at least 8 characters long.

○       Contains both uppercase and lowercase letters.

○       Contains at least one digit (0-9).

○       Contains at least one special character (e.g., !, @, #, $, %).

●       The function should return a boolean value indicating whether the password meets the criteria.

●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

●       Provide appropriate feedback to the user based on the strength of the password. 
'''

def check_password_strength(password):
    # Check the minimum length
    if len(password) < 8:
        return False

    # Check if it contains both uppercase and lowercase letters
    if not any(i.isupper() for i in password) or not any(i.islower() for i in password):
        return False

    # Check if it contains at least one digit
    if not any(i.isdigit() for i in password):
        return False

    # Check if it contains at least one special character
    special_characters = ['!', '@', '#', '$', '%']
    if not any(i in special_characters for i in password):
        return False

    # If all criteria are met, return True
    return True

password = input("Enter a password: ")
if check_password_strength(password):
    print("Password is strong.")
else:
    print("Password is weak.")

    