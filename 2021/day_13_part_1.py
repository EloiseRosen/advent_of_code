marks, folds = open('input.txt').read().split('\n\n')
marks = marks.split('\n')
folds = folds.split('\n')

# get grid dimensions
first_x_fold = None
first_y_fold = None
for fold in folds:
    fold = fold[11:]
    direction, size = fold.split('=')
    if first_x_fold is None and direction == 'x':
        first_x_fold = int(size)
    if first_y_fold is None and direction == 'y':
        first_y_fold = int(size)
    if first_x_fold and first_y_fold:
        break
original_width = first_x_fold*2 + 1
original_height = first_y_fold*2 + 1

# populate starting grid
grid = [['.' for w in range(0, original_width)] for h in range (0, original_height)]
for mark in marks:
    col, row = map(int, mark.split(','))
    grid[row][col] = '#'

# do folds
folds = folds[:1]  # for part 1 keep only the first fold
for fold in folds:
    fold = fold[11:]
    direction, size = fold.split('=')
    size = int(size)
    if direction == 'y':  # fold is horizontal line, folding up
        one = [grid[i] for i in range(0, size)]
        two = [grid[i] for i in range(size+1, len(grid))]
        two = two[::-1]  # flip up
    elif direction == 'x':  # fold is vertical line, folding left
        one = [grid[row][:size] for row in range(0, len(grid))]
        two = [grid[row][size+1:] for row in range(0, len(grid))]
        two = [row[::-1] for row in two]  # flip left
    for row_idx in range(0, len(one)):
        for col_idx in range(0, len(one[0])):
            if two[row_idx][col_idx] == '#':
                one[row_idx][col_idx] = '#'
    grid = one

# count hashtags
ans = 0
for row_idx in range(0, len(grid)):
    for col_idx in range(0, len(grid[0])):
        if grid[row_idx][col_idx] == '#':
            ans += 1
print(ans)
