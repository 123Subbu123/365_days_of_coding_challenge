## 64.Tic-Tac-Toe

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")

# Function to check for a win
def check_win(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if (board[i] == board[i + 3] == board[i + 6] == player) or \
           (board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player):
            return True
    if (board[0] == board[4] == board[8] == player) or \
       (board[2] == board[4] == board[6] == player):
        return True
    return False

# Main game loop
current_player = "X"
is_game_over = False

print("Welcome to Tic-Tac-Toe!")
print_board()

while not is_game_over:
    try:
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if 0 <= move < 9 and board[move] == " ":
            board[move] = current_player
            print_board()
            if check_win(current_player):
                print(f"Player {current_player} wins! Congratulations!")
                is_game_over = True
            elif " " not in board:
                print("It's a tie! The game is over.")
                is_game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    except ValueError:
        print("Invalid input. Enter a number between 1 and 9.")

print("Thanks for playing Tic-Tac-Toe!")
