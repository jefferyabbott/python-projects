import random

# Function to print the board
def print_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Function to check for a win
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check for a tie
def check_tie(board):
    return all(spot != ' ' for spot in board)

# Function to get the user's move
def get_user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Function to get the computer's move
def get_computer_move(board):
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(available_moves)

# Main function to run the game
def tic_tac_toe():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # User's turn
        user_move = get_user_move(board)
        board[user_move] = 'X'
        print_board(board)

        if check_win(board, 'X'):
            print("You win!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

        # Computer's turn
        print("Computer's turn...")
        computer_move = get_computer_move(board)
        board[computer_move] = 'O'
        print_board(board)

        if check_win(board, 'O'):
            print("Computer wins!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()

