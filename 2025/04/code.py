import pathlib

data = pathlib.Path("2025/04/input.txt").read_text(encoding="utf-8")

grid = [list(line) for line in data.split("\n")]
NUM_ROWS = len(grid)
NUM_COLS = len(grid[0])
EIGHT_DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def count_neighbors(grid, row, col):
    """Count '@' neighbors for a cell."""
    neighbor_count = 0
    for delta_row, delta_col in EIGHT_DIRECTIONS:
        neighbor_row, neighbor_col = row + delta_row, col + delta_col
        if 0 <= neighbor_row < NUM_ROWS and 0 <= neighbor_col < NUM_COLS and grid[neighbor_row][neighbor_col] == '@':
            neighbor_count += 1
    return neighbor_count

# Find all '@' positions once
at_sign_positions = {(row, col) for row, grid_row in enumerate(grid) for col, cell in enumerate(grid_row) if cell == '@'}

# Part 1: Count cells with < 4 neighbors in original state
part_1 = sum(1 for row, col in at_sign_positions if count_neighbors(grid, row, col) < 4)

# Part 2: Make a copy and simulate removal
grid_copy = [row[:] for row in grid]
active_positions = at_sign_positions.copy()
part_2 = 0

while active_positions:
    positions_to_remove = {(row, col) for row, col in active_positions if count_neighbors(grid_copy, row, col) < 4}
    if not positions_to_remove:
        break
    for row, col in positions_to_remove:
        grid_copy[row][col] = '.'
    part_2 += len(positions_to_remove)
    active_positions -= positions_to_remove
    
print(part_1)
print(part_2)  