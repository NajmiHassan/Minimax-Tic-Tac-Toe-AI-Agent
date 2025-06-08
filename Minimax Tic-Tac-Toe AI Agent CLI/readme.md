# 🎮 Tic-Tac-Toe AI Agent

This is a simple command-line Tic-Tac-Toe game where a human player can challenge an unbeatable AI opponent. The AI utilizes the **Minimax algorithm** to determine its optimal moves, ensuring it will never lose a game (it will either win or draw).

---

## ✨ Features

* **Human vs. AI Gameplay:** Play against a smart AI.

* **Unbeatable AI:** The AI uses the Minimax algorithm to play optimally, meaning it will always make the best possible move to win or force a draw.

* **Command-Line Interface:** Simple text-based interaction for easy setup and play.

* **Clear Board Display:** A visual representation of the 3x3 game board.

* **Turn-Based:** Players take turns making moves.

---

## 🧠 How the AI Works (Minimax Algorithm)

The core of this AI lies in the **Minimax algorithm**. Here's a simplified explanation:

1.  **Exploration:** The AI looks ahead at all possible future moves from the current game state.

2.  **Simulation:** For each possible move, it simulates the opponent's best response, and then its own best response to that, and so on, until the game ends (win, loss, or draw).

3.  **Scoring:**

    * If the AI finds a path to a win, it assigns a positive score (+1).

    * If it finds a path where the human wins, it assigns a negative score (-1).

    * A draw results in a score of 0.

4.  **Decision:**

    * The AI (the "maximizing" player) chooses the move that leads to the highest possible score for itself.

    * The human (the "minimizing" player) is assumed to choose the move that leads to the lowest possible score for the AI.

5.  **Optimal Play:** By recursively applying this evaluation to all possible game outcomes, the AI can always select a move that guarantees it the best possible result, preventing any losses.

---

## 🚀 How to Run

To get this game up and running on your system, follow these simple steps:

1.  **Prerequisites:**

    * Ensure you have **Python 3** installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2.  **Save the Code:**

    * Copy the entire Python code provided previously.

    * Save it to a file named `tic_tac_toe_ai.py` (or any name ending with `.py`).

3.  **Execute the Game:**

    * Open your terminal or command prompt.

    * Navigate to the directory where you saved `tic_tac_toe_ai.py`.

    * Run the script using the Python interpreter:

        ```bash
        python tic_tac_toe_ai.py
        ```

4.  **Play!**

    * Follow the on-screen prompts. You'll be asked to enter a number from `0` to `8` corresponding to the position on the board where you want to place your 'X'.

Enjoy playing against your unbeatable AI!
