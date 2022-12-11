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


def ticTacToe(board):
    return


printBoard(theBoard)
