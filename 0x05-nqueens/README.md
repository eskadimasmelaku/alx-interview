0x05. N Queens
Overview
This project solves the N Queens problem, where N queens must be placed on an N x N chessboard such that no two queens threaten each other. The solution utilizes a backtracking algorithm implemented in Python.

Requirements
OS: Ubuntu 20.04 LTS
Python: 3.4.3
Style: PEP 8 (version 1.7.*)
Editor: vi, vim, emacs
Usage
Run the program with:
./0-nqueens.py N
Where N is an integer >= 4. Each solution outputs a list of lists, with each inner list showing the [row, column] of a queen.

Example
bash
Copy code
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
Input Validation
If no N is provided, or N is invalid, the program shows an error message:
Usage: nqueens N if no argument is given.
N must be a number if N is not an integer.
N must be at least 4 if N < 4.
Concepts
Backtracking: Explores possible solutions, backtracking when a path is invalid.
Recursion: Places queens row by row.
List Manipulations: Manages board and queen positions.
