# helper: show start messae at app start h
def start_message():
    print("\nWelcome to Music Trivia. Please login ")
    print("or register to play a game.")

# display ui for game menu
def show_home():
    print("\n=============== Music Trivia ===============")
    print("--------------------------------------------")
    print("|   1.  Login         |   2.  Register     |")
    print("--------------------------------------------")
    print("|   3.  Play Game     |   4.  High Scores  |")
    print("--------------------------------------------")
    print("|   5.  Log Out       |   6.  Quit         |")
    print("--------------------------------------------\n")

# helper: prompt user to press enter to continue
def keep_going():
    input("Press enter to continue...")