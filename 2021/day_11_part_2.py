grid = [list(map(int, row)) for row in open('input.txt').read().split('\n')]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

step = 1
while True:
    # the energy level of each octopus increases by 1
    for row_idx in range(0, len(grid)):
        for col_idx in range(0, len(grid[0])):
            grid[row_idx][col_idx] += 1

    # flashes
    has_flashed = [[False]*len(grid[0]) for row in grid]
    grid_has_changed = True
    while grid_has_changed:
        grid_has_changed = False
        for row_idx in range(0, len(grid)):
            for col_idx in range(0, len(grid[0])):
                if grid[row_idx][col_idx] > 9 and not has_flashed[row_idx][col_idx]:
                    grid_has_changed = True
                    has_flashed[row_idx][col_idx] = True
                    for row_change, col_change in dirs:
                        new_row_idx = row_idx + row_change
                        new_col_idx = col_idx + col_change
                        if (new_row_idx >= 0 and new_row_idx < len(grid) and 
                        new_col_idx >= 0 and new_col_idx < len(grid[0])):
                            grid[new_row_idx][new_col_idx] += 1
                            
    # any octopus that flashed during this step has its energy level set to 0
    all_flashed = True
    for row_idx in range(0, len(grid)):
        for col_idx in range(0, len(grid[0])):
            if has_flashed[row_idx][col_idx]:
                grid[row_idx][col_idx] = 0
            else:
                all_flashed = False

    if all_flashed:
        break

    step += 1

print(step)
