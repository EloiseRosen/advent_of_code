lst = [row.split(' -> ') for row in open('input.txt').read().split('\n')]
SAND_START = [0, 500]

# clean up, get dimensions
min_row, max_row, min_col, max_col = SAND_START[0], SAND_START[0], SAND_START[1], SAND_START[1]
for line_idx, line in enumerate(lst):
    for item_idx, item in enumerate(line):
        col, row = map(int, item.split(','))
        lst[line_idx][item_idx] = (row, col)
        min_row, max_row = min(min_row, row), max(max_row, row)
        min_col, max_col = min(min_col, col), max(max_col, col)
col_offset = min_col - 1  # -1 due to out of bounds padding added below
row_offset = min_row

# make grid
# x's around perimeter mark spots from which sand falls forever
grid = [['x']+['.' for i in range(min_col, max_col+1)]+['x']
                for row in range(min_row, max_row+1)]
grid.append(['x' for i in range(min_col, max_col+1+2)])
for line in lst:
    for idx in range(0, len(line)-1):
        start_row, start_col = line[idx]
        end_row, end_col = line[idx+1]
        assert (start_row == end_row or start_col == end_col)
        if start_row == end_row:
            for col in range(min(start_col, end_col), max(start_col, end_col)+1):
                grid[start_row-row_offset][col-col_offset] = '#'
        elif start_col == end_col:
            for row in range(min(start_row, end_row), max(start_row, end_row)+1):
                grid[row-row_offset][start_col-col_offset] = '#'    

# drop sand
dirs = [(1, 0), (1, -1), (1, 1)]  # sands first tries to move down, then down-left, then down-right
num_drops = 0
infinite_fall = False
while not infinite_fall:
    row, col = SAND_START
    row = row - row_offset
    col = col - col_offset
    final_resting_place = False
    while not final_resting_place and not infinite_fall:
        final_resting_place = True
        for row_change, col_change in dirs:
            new_row = row + row_change
            new_col = col + col_change
            if grid[new_row][new_col] == 'x':  # sand goes to a spot from which it falls forever
                print(num_drops)
                infinite_fall = True
                break

            if grid[new_row][new_col] == '.':
                row = new_row
                col = new_col
                final_resting_place = False  # the sand was able to find a spot further down it can go
                break

    if final_resting_place and not infinite_fall:
        grid[row][col] = 'o'
        num_drops += 1
