"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Pavlína Nováková
email: spiki15@seznam.cz
discord: Pavlína Nováková (pavlinanovakova)
"""

# úvod
print("Welcome to Tic Tac Toe")
print("============================================")
print("GAME RULES:")
print("""Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row""")
print("============================================")
print("Let's start the game")
print("--------------------------------------------")


# hrací plocha
field = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

game_running = True
winner = None
current_player = "O"

def print_field():
    print("+---+---+---+")
    print("| " + field[0] + " | " + field[1] + " | " + field[2] + " | ")
    print("+---+---+---+")
    print("| " + field[3] + " | " + field[4] + " | " + field[5] + " | ")
    print("+---+---+---+")
    print("| " + field[6] + " | " + field[7] + " | " + field[8] + " | ")
    print("+---+---+---+")


# definice hry
def play_game():
    print_field()
    while game_running:
        handle_turn(current_player)
        check_game_over()
        switch_player()
    if winner == "O" or winner == "X":
        print("============================================")
        print(f"Congratulations, the player {winner} WON!")
        print("============================================")
    elif winner == None:
        print("============================================")
        print("Draw!")
        print("============================================")


def handle_turn(player):
    print("============================================")
    position = input(f"Player {player} | Please enter your move number: ")
    print("============================================")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
            print("============================================")
        position = int(position) - 1
        if field[position] == " ":
            valid = True
        else:    
            print("Invalid position. Please try again: ")
            print("============================================")
    field[position] = player
    print_field()
    

def check_game_over():
    check_winner()
    check_draw()


def check_winner():
    global winner
    horizontal_winner = check_horizontal()
    vertical_winner = check_vertical()
    diagonal_winner = check_diagonal()
    if horizontal_winner:
        winner = horizontal_winner
    elif vertical_winner:
        winner = vertical_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_horizontal():
    global game_running
    horizontal_1 = field[0] == field[1] == field[2] != " "
    horizontal_2 = field[3] == field[4] == field[5] != " "
    horizontal_3 = field[6] == field[7] == field[8] != " "
    if horizontal_1 or horizontal_2 or horizontal_3:
        game_running = False
    if horizontal_1:
        return field[0]
    elif horizontal_2:
        return field[3]
    elif horizontal_3:
        return field[6]
    return

def check_vertical():
    global game_running
    vertical_1 = field[0] == field[3] == field[6] != " "
    vertical_2 = field[1] == field[4] == field[7] != " "
    vertical_3 = field[2] == field[5] == field[8] != " "
    if vertical_1 or vertical_2 or vertical_3:
        game_running = False
    if vertical_1:
        return field[0]
    elif vertical_2:
        return field[1]
    elif vertical_3:
        return field[2]
    return

def check_diagonal():
    global game_running
    diagonal_1 = field[0] == field[4] == field[8] != " "
    diagonal_2 = field[6] == field[4] == field[2] != " "
    if diagonal_1 or diagonal_2:
        game_running = False
    if diagonal_1:
        return field[0]
    elif diagonal_2:
        return field[6]
    return

def check_draw():
    global game_running
    if " " not in field:
        game_running = False
    return


def switch_player():
    global current_player
    if current_player == "O":
        current_player = "X"
    elif current_player == "X":
        current_player = "O"
    return


play_game()