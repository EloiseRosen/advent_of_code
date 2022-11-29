grid = open('input.txt').read().split('\n')
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

ans = 0
for row_idx in range(0, len(grid)):
    for col_idx in range(0, len(grid[0])):
        is_low_point = True
        for row_change, col_change in dirs:
            new_row_idx = row_idx + row_change
            new_col_idx = col_idx + col_change
            if (new_row_idx >= 0 and new_row_idx < len(grid) and 
            new_col_idx >= 0 and new_col_idx < len(grid[0])):
                if int(grid[new_row_idx][new_col_idx]) <= int(grid[row_idx][col_idx]):
                    is_low_point = False
                    break
        if is_low_point:
            ans += (1+int(grid[row_idx][col_idx]))

print(ans)
