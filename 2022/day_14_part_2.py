lst = [row.split(' -> ') for row in open('input.txt').read().split('\n')]
SAND_START = [0, 500]

# clean up, get dimensions
min_row, max_row = SAND_START[0], SAND_START[0]
for line_idx, line in enumerate(lst):
    for item_idx, item in enumerate(line):
        col, row = map(int, item.split(','))
        lst[line_idx][item_idx] = (row, col)
        min_row, max_row = min(min_row, row), max(max_row, row)
# In the most expansive case, we take a step left every time we take a step down, or we take
# a step right every time we take a step down. So (max_row-min_row)+2 is the max number of steps
# we can end up left or right from the source of the sand. (The +2 is from the 2 extra lines we 
# add to the bottom of the grid in part 2.
max_dist_from_start = (max_row-min_row)+2
width = 1 + max_dist_from_start*2
col_offset = SAND_START[1] - max_dist_from_start
row_offset = min_row

# make grid
grid = [['.' for i in range(0, width)]
                for row in range(min_row, max_row+1)]
# for part 2, add 1 empty line then floor
grid.append(['.' for i in range(0, width)])
grid.append(['#' for i in range(0, width)])
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
full = False
while not full:
    row, col = SAND_START
    row = row - row_offset
    col = col - col_offset
    final_resting_place = False
    while not final_resting_place and not full:
        final_resting_place = True
        # go through the 3 possible directions it can move, going in the first one that works
        for row_change, col_change in dirs:
            new_row = row + row_change
            new_col = col + col_change
            if grid[new_row][new_col] == '.':
                row = new_row
                col = new_col
                final_resting_place = False  # the sand was able to find a spot further down it can go
                break

        if row == SAND_START[0] - row_offset:
            grid[row][col] = 'o'
            num_drops += 1
            full = True
            print(num_drops)

    if final_resting_place and not full:
        grid[row][col] = 'o'
        num_drops += 1
