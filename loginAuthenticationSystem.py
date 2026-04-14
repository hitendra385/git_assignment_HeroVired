def validate_login(username, password):
    if len(username) < 5:
        print("Username must be at least 5 characters.")
        return False
    if len(password) < 8:
        print("Password must be at least 8 characters.")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False
    
    print("Login successful!")
    return True

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
validate_login(input_username, input_password)