# register workflow

def register(database):
    # prompt for username with validation logic
    while True:
        username = input("\nEnter a username: ")
        if len(username) < 4 or len(username) > 8:
            print("Username must be between 4 and 8 characters.")
            continue
        if username in database:
            print("\nThis username is already taken.")
            print("Please choose another username.  ")
        else:
            break
    # prompt for password with validation logic
    while True:
        password = input("Enter a password: ")
        if len(password) < 4 or len(password) > 8:
            print("\nPassword must be between 4 and 8 characters.\n")
        else:
            database[username] = password
            print(f"\nUser {username.capitalize()} successfully registered.\n")
            break


def login(database):
    # initialize authorized_user
    authorized_user = None  
    print("\nEnter your username and password to login...\n")
   
    while authorized_user is None:
        if authorized_user:
            print(f"\nYou are already logged in as {authorized_user.capitalize()}.")
            print("Please try another option.\n")
            break

        username = input("Username: ")
        username = username.lower()
        password = input("Password: ")
        
        if username in database:
            if database[username] == password:
                authorized_user = username
                print(f"\nWelcome, {authorized_user.capitalize()}. You are now logged in.")
                print(f"Shall we play a game?\n")
            else: 
                print("\nAccess denied. You entered an incorrect password.")
                print("Enter your username and password to login...\n")
        else:
            print("\nAccess denied. You entered an incorrect username.")
            print("Enter your username and password to login...\n")

    return authorized_user

def logout(authorized_user):
    if authorized_user:
        print(f"\nGoodbye, {authorized_user.capitalize()}.")
        print("You are now logged out.\n")
        authorized_user = ""
    else:
        print("\nYou are not logged in.")
        print("Please try another option.\n")
    return authorized_user

