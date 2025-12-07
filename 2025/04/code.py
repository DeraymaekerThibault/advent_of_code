import pathlib

data = pathlib.Path("2025/04/input.txt").read_text(encoding="utf-8")

grid = [list(line) for line in data.split("\n")]
ROWS = len(grid)
COLS = len(grid[0])
NEIGH_8 = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def count_neighbors(grid, r, c):
    """Count '@' neighbors for a cell."""
    count = 0
    for dr, dc in NEIGH_8:
        cr, cc = r + dr, c + dc
        if 0 <= cr < ROWS and 0 <= cc < COLS and grid[cr][cc] == '@':
            count += 1
    return count

# Find all '@' positions once
at_positions = {(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == '@'}

# Part 1: Count cells with < 4 neighbors in original state
part_1 = sum(1 for r, c in at_positions if count_neighbors(grid, r, c) < 4)

# Part 2: Make a copy and simulate removal
grid_copy = [row[:] for row in grid]
active = at_positions.copy()
part_2 = 0

while active:
    to_remove = {(r, c) for r, c in active if count_neighbors(grid_copy, r, c) < 4}
    if not to_remove:
        break
    for r, c in to_remove:
        grid_copy[r][c] = '.'
    part_2 += len(to_remove)
    active -= to_remove
    
print(part_1)
print(part_2)  