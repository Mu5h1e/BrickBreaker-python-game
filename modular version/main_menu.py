from game_functions import start_game


def show_main_menu():
    print("Press ENTER to Start Game")
    print("Press Q to Quit")

    gameChoice = input("")
    if gameChoice == "":
        start_game()
    elif gameChoice == "Q":
        print("Thanks for Playing")
    else:
        print("Incorrect Choice")
        showMainMenu()