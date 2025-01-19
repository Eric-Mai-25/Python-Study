def solve_n_queens(n: int) -> list[list[str]]:
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == "Q": return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == "Q": return False
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == "Q": return False
        return True
    
    def solve(row):
        if row == n:
            result.append(["".join(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = "Q"
                solve(row + 1)
                board[row][col] = "."  # Backtrack
    
    result = []
    board = [["."] * n for _ in range(n)]
    solve(0)
    return result

# Example
solutions = solve_n_queens(4)
for solution in solutions:
    print("\n".join(solution))
    print()