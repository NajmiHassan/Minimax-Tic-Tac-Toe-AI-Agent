import streamlit as st
from tic_tac_toe_ai import create_board, make_move, find_best_move, get_game_status

# Initialize session state
if 'board' not in st.session_state:
    st.session_state.board = create_board()
if 'current_player' not in st.session_state:
    st.session_state.current_player = 'X'
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'ai_move_made' not in st.session_state:
    st.session_state.ai_move_made = False

def reset_game():
    """Reset the game to initial state"""
    st.session_state.board = create_board()
    st.session_state.current_player = 'X'
    st.session_state.game_over = False
    st.session_state.ai_move_made = False

def display_board():
    """Display the Tic-Tac-Toe board using buttons"""
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            position = row * 3 + col
            with cols[col]:
                cell_value = st.session_state.board[position]
                display_value = cell_value if cell_value != ' ' else ''
                
                # Only allow clicking if cell is empty and game is not over and it's human's turn
                if (cell_value == ' ' and 
                    not st.session_state.game_over and 
                    st.session_state.current_player == 'X'):
                    if st.button(display_value, key=f"cell_{position}", 
                               help=f"Position {position}"):
                        # Human makes move
                        if make_move(st.session_state.board, position, 'X'):
                            st.session_state.current_player = 'O'
                            st.rerun()
                else:
                    # Display as disabled button or just text
                    st.button(display_value, key=f"cell_{position}", 
                            disabled=True)

def make_ai_move():
    """Make AI move if it's AI's turn"""
    if (st.session_state.current_player == 'O' and 
        not st.session_state.game_over and 
        not st.session_state.ai_move_made):
        
        ai_move = find_best_move(st.session_state.board)
        if ai_move != -1:
            make_move(st.session_state.board, ai_move, 'O')
            st.session_state.current_player = 'X'
            st.session_state.ai_move_made = True
            st.rerun()

# Main app
st.title("🎮 Tic-Tac-Toe vs AI")
st.markdown("You are **X**, AI is **O**. Click on empty cells to make your move!")

# Display current game status
game_status = get_game_status(st.session_state.board)

if game_status == 'X_wins':
    st.success("🎉 Congratulations! You (X) won!")
    st.session_state.game_over = True
elif game_status == 'O_wins':
    st.error("🤖 AI (O) wins! Better luck next time!")
    st.session_state.game_over = True
elif game_status == 'draw':
    st.info("🤝 It's a draw!")
    st.session_state.game_over = True
elif st.session_state.current_player == 'X':
    st.info("Your turn (X)")
elif st.session_state.current_player == 'O':
    st.info("AI is thinking... (O)")

# Display the game board
display_board()

# Make AI move if it's AI's turn
if st.session_state.current_player == 'O' and not st.session_state.game_over:
    make_ai_move()

# Reset AI move flag when it's human's turn
if st.session_state.current_player == 'X':
    st.session_state.ai_move_made = False

# Reset button
st.divider()
if st.button("🔄 New Game", type="primary"):
    reset_game()
    st.rerun()

# Instructions
with st.expander("ℹ️ How to Play"):
    st.markdown("""
    1. You are **X** and the AI is **O**
    2. Click on any empty cell to make your move
    3. The AI will automatically make its move after yours
    4. Get three in a row (horizontally, vertically, or diagonally) to win!
    5. The AI uses the Minimax algorithm, so it's quite challenging to beat!
    """)

# Board position reference
with st.expander("📍 Board Positions"):
    st.markdown("""
    ```
     0 | 1 | 2 
    ---+---+---
     3 | 4 | 5 
    ---+---+---
     6 | 7 | 8 
    ```
    """)
