# Tic-Tac-Toe AI Game

A web-based Tic-Tac-Toe game where you play against an unbeatable AI opponent. Built with Python and Streamlit.

## Features

- Interactive web interface using Streamlit
- Unbeatable AI using the Minimax algorithm
- Clean separation between game logic and UI
- Real-time game status updates
- Easy reset functionality

## Files Structure

```
├── tic_tac_toe_ai.py    # Core game logic and AI implementation
├── app.py               # Streamlit web application
└── README.md           # This file
```

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependency:
   ```bash
   pip install streamlit
   ```

## How to Run

1. Clone or download the project files
2. Open terminal/command prompt in the project directory
3. Run the application:
   ```bash
   streamlit run app.py
   ```
4. The game will open in your default web browser

## How to Play

1. You are **X** and the AI is **O**
2. Click on any empty cell to make your move
3. The AI will automatically make its move after yours
4. Get three in a row (horizontally, vertically, or diagonally) to win
5. Click "New Game" to start over

## Game Logic

### Core Components

- **Board Representation**: 3x3 grid stored as a list of 9 elements
- **Move Validation**: Ensures moves are made only on empty cells
- **Win Detection**: Checks all possible winning combinations
- **Draw Detection**: Identifies when the board is full with no winner

### AI Implementation

The AI uses the **Minimax Algorithm** with the following approach:

- **Maximizing Player**: AI (O) tries to maximize its score
- **Minimizing Player**: Human (X) tries to minimize AI's score
- **Scoring System**: +1 for AI win, -1 for human win, 0 for draw
- **Optimal Play**: AI explores all possible future game states

This makes the AI unbeatable - it will either win or draw, never lose.

## Technical Details

### Dependencies

- **Python 3.7+**
- **Streamlit**: For the web interface

### Session State Management

The Streamlit app uses session state to maintain:
- Current board state
- Active player turn
- Game over status
- AI move tracking

## Board Position Reference

```
 0 | 1 | 2 
---+---+---
 3 | 4 | 5 
---+---+---
 6 | 7 | 8 
```

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

### Made by Najmi Hassan
