# Tic Tac Toe Game

# ------- Global Variables ------------

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

# Is the game still going
game_still_going = True

# who won or tie?
winner = None

# who's turn is it
current_player = "X"


def display_board():
    print("1 | 2 | 3    " + board[0] + " | " + board[1] + " | " + board[2])
    print("4 | 5 | 6    " + board[3] + " | " + board[4] + " | " + board[5])
    print("7 | 8 | 9    " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def play_game():
    # display initial board
    display_board()

    while game_still_going:

        # hanlde a single turn of arbitrary player
        handle_turn(current_player)

        # Check if game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

        # The game has ended
        if winner == "X" or winner == "O":
            print(winner + " Won. Congrats!")
        elif not game_still_going and winner == None:
            print('Tie.')

# hanlde a single turn of arbitrary player


def handle_turn(player):

    print(player, "'s turn")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Try again")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    global winner
    # check rows, colums and diagonals
    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return

# check the rows if there is any win


def check_rows():

    global game_still_going

    # check if any of the rows have same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    # return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

# check the columns if there is any win


def check_columns():
    global game_still_going

    # check if any of the rows have same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    # return the winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

# check the diagonals if there is any win


def check_diagonals():
    global game_still_going

    # check if any of the rows have same value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return the winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

# check if the game is a tie


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

    return

# to change the player from X to O or vice versa after a turn


def flip_player():
    global current_player

    # if current was X change to O
    if current_player == "X":
        current_player = "O"
    # if current was O change to X
    elif current_player == "O":
        current_player = "X"
    return


# start the game
play_game()
