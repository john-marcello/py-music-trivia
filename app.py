import sys
from data_pkg.data import get_data
from ui_pkg.home import keep_going, show_home, start_message
from auth_pkg.user import login, logout, register
from game_pkg.play import play_game

# set up user db and initialize authorized user
database = {"admin": "pass"}
authorized_user = ""

# set up data, start message, home page
get_data()
start_message()
show_home()

# loop to drive the home page menu
# execute workflows for each option
while True:
    option = (input("Choose an option: "))
    
    # login user flow
    if option == "1":
        if authorized_user:
            print(f"\nYou are already logged in as {authorized_user.capitalize()}.")
            print("Please try another option.\n")
        else:
            authorized_user = login(database)
            if authorized_user:
                keep_going()
                show_home()

    # register user flow
    elif option == "2":
        if authorized_user:
            print("\nYou must log out to register.")
            print("Press 5 to logout.\n")
        else:
            register(database)
            keep_going()
            show_home()
    
    # game play flow
    elif option == "3":
        if authorized_user:
            play_game()
            keep_going()
            show_home()
        else:             
            print(f"\nYou must be logged in to play a game.")
            print("Press 1 to login.\n")
            
    # high score flow
    elif option == "4":
        print("\nBuild out high score feature\n")

    # log out flow
    elif option == "5":
        authorized_user = logout(authorized_user)
        keep_going()
        show_home()

    # exit flow
    elif option == "6":
        if authorized_user:
            print(f"\nGoodbye, {authorized_user.capitalize()}. We are exiting the program. Come again soon.\n")
        else:
            print(f"\nGoodbye. We are exiting the program. Come again soon.\n")
        sys.exit(0)

    # non-happy path
    else:
        print("\nInvalid entry, please try again\n")


