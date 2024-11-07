#!/usr/bin/python3
import sys

def print_solution(solution):
    """Prints a single solution in the required format."""
    print(solution)

def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, solutions):
    """Utilizes backtracking to find all solutions for the N Queens problem."""
    if col == len(board):
        # All queens are placed
        solution = [[i, row.index(1)] for i, row in enumerate(board)]
        solutions.append(solution)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, solutions)
            board[i][col] = 0  # Backtrack

def solve_nqueens(n):
    """Sets up the board and starts the solution process."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions

if __name__ == "__main__":
    # Input validation
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve and print all solutions
    solutions = solve_nqueens(n)
    for solution in solutions:
        print_solution(solution)
