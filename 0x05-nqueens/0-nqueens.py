#!/usr/bin/python3
"""
Try and solve the N Queens problem
"""

import sys


def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    queens = [-1] * n
    solutions = []
    solve(queens, 0, n, solutions)
    for solution in solutions:
        positions = [[i, q] for i, q in enumerate(solution)]
        print(positions)


def solve(queens, row, n, solutions):
    if row == n:
        solutions.append(list(queens))
    else:
        for col in range(n):
            if is_valid(queens, row, col):
                queens[row] = col
                solve(queens, row + 1, n, solutions)


def is_valid(queens, row, col):
    for r in range(row):
        c = queens[r]
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_nqueens(n)
