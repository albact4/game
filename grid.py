def is_valid_move(x, y, grid):
    """Check if the move is within the grid bounds and the square is empty."""
    return 0 <= x < 6 and 0 <= y < 6 and grid[x][y] == 0

def solve(grid, x, y, move_number, moves):
    """Recursive backtracking function to fill the grid."""
    if move_number > 36:
        return True  # All numbers placed

    # Check all possible moves (3 horizontal, 3 vertical, 2 diagonal)
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y, grid):
            grid[new_x][new_y] = move_number  # Place the number
            if solve(grid, new_x, new_y, move_number + 1, moves):
                return True
            # Backtrack
            grid[new_x][new_y] = 0

    return False

def fill_grid():
    # Initialize a 6x6 grid with all zeros
    grid = [[0 for _ in range(6)] for _ in range(6)]

    # Possible moves: (3 horizontal, 3 vertical, 2 diagonal)
    moves = [
        (3, 0), (-3, 0),  # Horizontal moves
        (0, 3), (0, -3),  # Vertical moves
        (2, 2), (2, -2), (-2, 2), (-2, -2)  # Diagonal moves
    ]

    # Start from any position, e.g., top-left corner (0, 0)
    start_x, start_y = 0, 0
    grid[start_x][start_y] = 1  # Place the first number

    if solve(grid, start_x, start_y, 2, moves):
        for row in grid:
            print(row)
    else:
        print("No solution found.")

fill_grid()
