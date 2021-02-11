from game_functions import start_game


def show_main_menu():
    print("Press ENTER to Start Game")
    print("Press Q to Quit")

    gameChoice = input("")
    if gameChoice == "":
        startGame()
    elif gameChoice == "Q":
        print("Thanks for Playing")
    else:
        print("Incorrect Choice")
        showMainMenu()