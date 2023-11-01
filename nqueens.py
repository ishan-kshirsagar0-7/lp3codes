from copy import deepcopy

# Check if a queen can be placed on board[row][col]
def is_safe(board, row, col, n):
    # Check this row on the left side
    for i in range(col):
        if board[row][i]:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    return True

# Main recursive function to solve N-Queens
def solve_n_queens_util(board, col, n):
    # Base case: If all queens are placed
    if col >= n:
        return [deepcopy(board)]
    
    solutions = []
    # Try placing queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            for solution in solve_n_queens_util(board, col + 1, n):
                solutions.append(deepcopy(solution))
            board[i][col] = 0  # backtrack
    
    return solutions

# Driver code
if __name__ == "__main__":
    n = 4  # Number of queens and size of board (n x n)
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Solve and get all possible solutions
    solutions = solve_n_queens_util(board, 0, n)
    
    # Print solutions
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in solution:
            print(" ".join(str(cell) for cell in row))
        print()