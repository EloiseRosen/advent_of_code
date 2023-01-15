from collections import  defaultdict


algorithm, grid = open('input.txt').read().split('\n\n')
grid = list(map(list, grid.split('\n')))

ITERATIONS = 50

DIRS = [(-1,-1), (-1,0), (-1,1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)]


def enhance(grid_defaultdict, default_value):
    new_default_value = '#' if default_value == '.' else '.'
    new_grid_defaultdict = defaultdict(lambda: new_default_value)

    row_min = min(grid_defaultdict.keys(), key=lambda x: x[0])[0]
    row_max = max(grid_defaultdict.keys(), key=lambda x: x[0])[0]
    col_min = min(grid_defaultdict.keys(), key=lambda x: x[1])[1]
    col_max = max(grid_defaultdict.keys(), key=lambda x: x[1])[1]
    # bounds: there's a 1 cell area beyond the marks in which cells may get marked 
    # as their 3x3 area  is in reach of a mark
    for row_idx in range(row_min-1, row_max+2):
        for col_idx in range(col_min-1, col_max+2):
            binary = ''
            for row_change, col_change in DIRS:
                new_row_idx = row_idx + row_change
                new_col_idx = col_idx + col_change
                if grid_defaultdict[(new_row_idx, new_col_idx)] == '#':
                    binary += '1'
                else:
                    binary += '0'
            idx = int(binary, 2)
            new_grid_defaultdict[(row_idx,col_idx)] = algorithm[idx]

    return new_grid_defaultdict, new_default_value


default_value = '.'
grid_defaultdict = defaultdict(lambda: default_value)
for row_idx in range(0, len(grid)):
    for col_idx in range(0, len(grid[0])):
        grid_defaultdict[(row_idx, col_idx)] = grid[row_idx][col_idx]

for _ in range(0, ITERATIONS):
    grid_defaultdict, default_value = enhance(grid_defaultdict, default_value)

ans = 0
for val in grid_defaultdict.values():
    if val == '#':
        ans += 1
print(ans)
