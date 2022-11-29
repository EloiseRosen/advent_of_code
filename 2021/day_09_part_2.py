import re

original_grid = open('input.txt').read().split('\n')
grid = [list(row[:]) for row in original_grid]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def flood_fill(grid, row_idx, col_idx):
    basin_size = 0
    if (row_idx >= 0 and col_idx >= 0 and row_idx < len(grid) and col_idx < len(grid[0]) 
    and grid[row_idx][col_idx] != '9'):
        basin_size += 1
        grid[row_idx][col_idx] = '9'
        for row_change, col_change in dirs:
            basin_size += flood_fill(grid, row_idx+row_change, col_idx+col_change)
    return basin_size


basin_sizes = []
for row_idx in range(0, len(grid)):  
    while (match_obj := re.search(r'[0-8]', ''.join(grid[row_idx]))) is not None:
        col_idx = match_obj.start()
        basin_size = flood_fill(grid, row_idx, col_idx)
        basin_sizes.append(basin_size)

top_3 = sorted(basin_sizes, reverse=True)[:3]
ans = 1
for el in top_3:
    ans *= el
print(ans)
