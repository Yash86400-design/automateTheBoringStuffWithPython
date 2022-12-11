import random

theBoard = {
    "top-L": " ", "top-M": " ", "top-R": " ",
    "mid-L": " ", "mid-M": " ", "mid-R": " ",
    "low-L": " ", "low-M": " ", "low-R": " ",
}

# So that I can show the user how many options left to fill.
list_of_options = ["top-L", "top-M", "top-R", "mid-L",
                   "mid-M", "mid-R", "low-L", "low-M", "low-R"]


def printBoard(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


def winnerAnnounce(board, userOption):
    # Make sure to pass X || O as second argument of this function.

    if (board["top-L"] == userOption and board["top-M"] == userOption and board["top-R"] == userOption):
        return f"{userOption} is winner"

    elif (board["mid-L"] == userOption and board["mid-M"] == userOption and board["mid-R"] == userOption):
        return f"{userOption} is winner"

    elif (board["low-L"] == userOption and board["low-M"] == userOption and board["low-R"] == userOption):
        return f"{userOption} is winner"

    elif (board["top-L"] == userOption and board["mid-M"] == userOption and board["low-R"] == userOption):
        return f"{userOption} is winner"

    elif (board["top-R"] == userOption and board["mid-M"] == userOption and board["low-L"] == userOption):
        return f"{userOption} is winner"

    elif (board["top-L"] == userOption and board["mid-L"] == userOption and board["low-L"] == userOption):
        return f"{userOption} is winner"

    elif (board["top-M"] == userOption and board["mid-M"] == userOption and board["low-M"] == userOption):
        return f"{userOption} is winner"

    elif (board["top-R"] == userOption and board["mid-R"] == userOption and board["low-R"] == userOption):
        return f"{userOption} is winner"

    else:
        return 0


def ticTacToe(board):
    # or hit enter to get 'O' as default value (apply it too)..
    computerWinnerCheck, userWinnerCheck = 0, 0
    usersValue = input("Select your player: 'O' or 'X': ")
    computerValue = "X"

    if usersValue == "X" or "x":
        print("Hi")
        computerValue = "O"
    
    i = 0
    while (i < 5):
        print(f"Where you want to put your {usersValue.capitalize()}")
        print(f"Available Inputs: ")
        for value in list_of_options:
            print(value, end=", ")
        print("\n")

        usersChoosenPlace = input()
        board[usersChoosenPlace] = usersValue
        list_of_options.remove(usersChoosenPlace)

        computerTurnIndex = random.randrange(len(list_of_options))
        computerChoosenPlace = list_of_options[computerTurnIndex]
        board[computerChoosenPlace] = computerValue
        list_of_options.remove(computerChoosenPlace)

        computerWinnerCheck = winnerAnnounce(board, computerValue)
        userWinnerCheck = winnerAnnounce(board, usersValue)

        printBoard(board)

        if (userWinnerCheck == 0 and computerWinnerCheck == 0):
            continue
        elif (userWinnerCheck != 0 and computerWinnerCheck == 0):
            print(userWinnerCheck)
            return
        elif (userWinnerCheck == 0 and computerWinnerCheck != 0):
            print(computerWinnerCheck)
            return


        i += 1

    print("It's an tie, Nobody won and peace prevailed")


printBoard(theBoard)
ticTacToe(theBoard)
