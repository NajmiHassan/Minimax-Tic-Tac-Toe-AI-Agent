import math

# --- Game Board & Basic Logic ---

def print_board(board):
    """
    Prints the Tic-Tac-Toe board in a readable 3x3 format.
    """
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print() # Add an empty line for better spacing

def make_move(board, position, player):
    """
    Attempts to place a player's marker on the board at the given position.
    Returns True if the move was valid, False otherwise.
    """
    if 0 <= position <= 8 and board[position] == ' ':
        board[position] = player
        return True
    return False

def check_win(board, player):
    """
    Checks if the specified player has won the game.
    """
    win_conditions = [
        # Rows
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Columns
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonals
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    """
    Checks if the game is a draw (no empty spaces and no winner).
    """
    return ' ' not in board and not check_win(board, 'X') and not check_win(board, 'O')

# --- Minimax Algorithm ---

def evaluate(board):
    """
    Evaluates the current state of the board for the minimax algorithm.
    Returns +1 if AI wins, -1 if Human wins, 0 for draw or game in progress.
    """
    if check_win(board, 'O'):  # AI wins
        return 1
    elif check_win(board, 'X'): # Human wins
        return -1
    else: # Draw or game still in progress
        return 0

def minimax(board, is_maximizing_player):
    """
    The Minimax algorithm function. Recursively explores game states
    to find the optimal move.

    :param board: The current state of the Tic-Tac-Toe board.
    :param is_maximizing_player: True if it's the AI's turn (maximizing player),
                                 False if it's the Human's turn (minimizing player).
    :return: The optimal score for the current player from this board state.
    """
    score = evaluate(board)

    # Base cases: if the game is over, return the score
    if score != 0: # Game is won or lost
        return score
    if check_draw(board): # Game is a draw
        return 0

    if is_maximizing_player: # AI's turn (O) - wants to maximize score
        best_eval = -math.inf # Initialize with negative infinity
        for i in range(9):
            if board[i] == ' ': # If the cell is empty
                board[i] = 'O' # Make a temporary move for 'O'
                eval = minimax(board, False) # Recurse for the minimizing player (X)
                board[i] = ' ' # Undo the move (crucial for exploring other branches)
                best_eval = max(best_eval, eval) # Take the maximum score
        return best_eval
    else: # Human's turn (X) - wants to minimize score (AI's score)
        best_eval = math.inf # Initialize with positive infinity
        for i in range(9):
            if board[i] == ' ': # If the cell is empty
                board[i] = 'X' # Make a temporary move for 'X'
                eval = minimax(board, True) # Recurse for the maximizing player (O)
                board[i] = ' ' # Undo the move
                best_eval = min(best_eval, eval) # Take the minimum score
        return best_eval

def find_best_move(board):
    """
    Determines the best move for the AI using the minimax algorithm.
    """
    best_eval = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == ' ': # For each empty spot
            board[i] = 'O' # Try making the AI's move
            # Calculate the score of this move assuming optimal play from human
            eval = minimax(board, False) # After AI's move, it's human's turn (minimizing)
            board[i] = ' ' # Undo the temporary move

            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# --- Game Loop ---

def play_game():
    """
    Manages the main game loop for Tic-Tac-Toe.
    """
    board = [' ' for _ in range(9)] # Initialize empty board
    current_player = 'X' # Human player (X) starts
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', the AI is 'O'.")
    print("Enter numbers 0-8 to make a move, corresponding to board positions:")
    print_board(['0', '1', '2', '3', '4', '5', '6', '7', '8']) # Show position mapping

    while not game_over:
        print_board(board)

        if current_player == 'X':
            try:
                move = int(input("Human (X), enter your move (0-8): "))
                if not (0 <= move <= 8) or not make_move(board, move, 'X'):
                    print("Invalid move. Position taken or out of range. Try again.")
                    continue # Ask for input again
            except ValueError:
                print("Invalid input. Please enter a number 0-8.")
                continue # Ask for input again
        else: # AI's turn
            print("AI (O) is thinking...")
            move = find_best_move(board)
            make_move(board, move, 'O')
            print(f"AI (O) chose position {move}")

        # Check for game end after every move
        if check_win(board, 'X'):
            print_board(board)
            print("Congratulations! Human (X) wins!")
            game_over = True
        elif check_win(board, 'O'):
            print_board(board)
            print("AI (O) wins! Better luck next time!")
            game_over = True
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            # Switch turns if game is not over
            current_player = 'O' if current_player == 'X' else 'X'

# --- Run the Game ---
if __name__ == "__main__":
    play_game()