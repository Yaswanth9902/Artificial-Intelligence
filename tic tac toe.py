# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Function to check if the board is full (draw)
def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])

# Function to handle the player's move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("That cell is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")

# Main function to run the game
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize the 3x3 board
    current_player = 'X'

    while True:
        print_board(board)
        player_move(board, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
