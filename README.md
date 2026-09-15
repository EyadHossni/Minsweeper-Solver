# Minsweeper-Solver
A Python/Pygame implementation of Minesweeper featuring an automated solver that analyzes the visible board and makes moves based on local mine-count constraints, with randomized selection used when no immediate deduction is available.

# Demo
https://github.com/user-attachments/assets/c7602bea-8866-4a58-93a8-2aa93b9a7706


# Features
- A resizable Minesweeper board
- Randomized mine placement
- Pygame-based graphical interface
- Mouse controls for opening and marking cells
- Automatic opening of adjacent empty cells
- Automated solver for making gameplay decisions
- Randomized fallback when no direct deduction can be made
- Win and game-over detection

# How the Solver Works
The solver examines the numbers revealed on the board and compares them with the currently known mines and unopened cells surrounding each number.

When the available information is sufficient, it can determine whether a neighboring cell should be:
- opened because it is safe, or
- marked because it contains a mine.

When no direct deduction is available, the solver selects an unopened cell randomly.

This approach combines simple constraint-based reasoning with controlled random selection rather than attempting to simulate human gameplay.

# Requirements
- Python 3.x
- Pygame

Install Pygame with: `pip install pygame`

# Running the Project
Clone the repository and run the main Python file: `python main.py`

The project also requires the accompanying game assets, including the board image/icon files used by the application.

## Controls
- Left mouse button: Open a cell
- Right mouse button: Mark a cell as a mine
- Backspace: Start the game
- Escape: Exit

# Project Purpose
*This project was developed as an exploration of game logic, grid-based data structures, recursive cell opening, and automated decision-making.*

*It was also an opportunity to experiment with implementing a game solver from scratch rather than relying on an existing Minesweeper-solving library.*

## Development
**No AI-generated code was used in the development of this project.**

The implementation, solver logic, and game mechanics were written manually as part of the project.

# License
This project is intended as a personal programming project and learning exercise.
