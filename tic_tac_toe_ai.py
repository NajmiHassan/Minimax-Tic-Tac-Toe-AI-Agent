import math

# --- Game Board & Basic Logic ---

def create_board():
    """
    Creates and returns an empty Tic-Tac-Toe board.
    """
    return [' ' for _ in range(9)]

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

def get_game_status(board):
    """
    Returns the current game status: 'X_wins', 'O_wins', 'draw', or 'ongoing'
    """
    if check_win(board, 'X'):
        return 'X_wins'
    elif check_win(board, 'O'):
        return 'O_wins'
    elif check_draw(board):
        return 'draw'
    else:
        return 'ongoing'

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
