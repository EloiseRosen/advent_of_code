import sys
sys.setrecursionlimit(100000)


DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
OPENINGS = {
            '|': {'above', 'below'},
            '-': {'left', 'right'},
            'L': {'above', 'right'},
            'J': {'above', 'left'},
            'F': {'below', 'right'},
            '7': {'below', 'left'},
            'S': {'above', 'below', 'left', 'right'}
            }


def is_valid(path, new, change):
    r, c = path[-1]
    new_r, new_c = new

    # on second move 'S' is still in range without been in seen set, so we need to prevent
    # doubling back
    if len(path) == 2 and grid[new_r][new_c] == 'S':
        return False

    curr_symbol = grid[r][c]
    new_symbol = grid[new_r][new_c]
    if new_symbol == '.':
        return False
    if change == (-1, 0):
        return 'above' in OPENINGS[curr_symbol] and 'below' in OPENINGS[new_symbol]
    if change == (1, 0):
        return 'below' in OPENINGS[curr_symbol] and 'above' in OPENINGS[new_symbol]
    if change == (0, -1):
        return 'left' in OPENINGS[curr_symbol] and 'right' in OPENINGS[new_symbol]    
    if change == (0, 1):
        return 'right' in OPENINGS[curr_symbol] and 'left' in OPENINGS[new_symbol]


def dfs(path):
    seen = set()
    def dfs_helper(path):
        curr = path[-1]
        r, c = curr

        if len(path) > 1: # don't add very first position, because we need to be able to move back to it
            seen.add(curr)

        if len(path) > 1 and grid[r][c] == 'S': # very first move we're already at start so don't check then
            return path

        for r_change, c_change in DIRS:
            new_r = r + r_change
            new_c = c + c_change
            if (new_r >= 0 and new_r < len(grid) and new_c >= 0 and new_c < len(grid[0])
            and (new_r, new_c) not in seen 
            and is_valid(path, (new_r, new_c), (r_change, c_change))):
                try_path = dfs_helper(path + [(new_r, new_c)])
                if try_path:
                    return try_path
        return []
    return dfs_helper(path)


def expand_grid(unexpanded_grid):
    expand_vertically = []
    for row_idx in range(0, len(unexpanded_grid)-1):
        row1 = unexpanded_grid[row_idx]
        row2 = unexpanded_grid[row_idx+1]
        expand_vertically.append(row1)
        new_row = []
        for col_idx in range(0, len(unexpanded_grid[0])):
            symbol_above = row1[col_idx]
            symbol_below = row2[col_idx]
            if (symbol_above != '.' and symbol_below != '.' 
                and 'below' in OPENINGS[symbol_above] and 'above' in OPENINGS[symbol_below]):
                new_row.append('|')
            else:
                new_row.append('.')
        expand_vertically.append(new_row)
    expand_vertically.append(unexpanded_grid[-1])
    grid = [[] for _ in range(0, len(expand_vertically))]
    for col_idx in range(0, len(expand_vertically[0])-1):
        for row_idx in range(0, len(expand_vertically)):
            val1 = expand_vertically[row_idx][col_idx]
            val2 = expand_vertically[row_idx][col_idx+1]
            grid[row_idx].append(val1)
            if (val1 != '.' and val2 != '.' 
                and 'right' in OPENINGS[val1] and 'left' in OPENINGS[val2]):
                grid[row_idx].append('-')
            else:
                grid[row_idx].append('.')
    for row_idx in range(0, len(expand_vertically)):
        grid[row_idx].append(expand_vertically[row_idx][-1])
    return grid


def flood_fill(grid, sr, sc):
    is_background = False
    spots = set()

    def dfs(r, c):
        grid[r][c] = 's' # mark seen
        spots.add( (r, c) )

        for r_change, c_change in DIRS:
            new_r = r + r_change
            new_c = c + c_change
            
            if new_r >= 0 and new_r < len(grid) and new_c >= 0 and new_c < len(grid[0]):
                if grid[new_r][new_c] == '.': # we can go here, and also this tile has not been seen
                    dfs(new_r, new_c)
            else:
                nonlocal is_background
                is_background = True

    dfs(sr, sc)
    return spots, is_background


# process into grid
grid = [list(r) for r in open('input.txt').read().split('\n')]

# get start position
start = None
for r_idx in range(0, len(grid)):
    for c_idx in range(0, len(grid[0])):
        if grid[r_idx][c_idx] == 'S':
            start = (r_idx, c_idx)
            break
    if start is not None:
        break

# get path
path = dfs(path=[start])

# mark any non-loop tiles as empty
for r in range(0, len(grid)):
    for c in range(0, len(grid[0])):
        if (r, c) not in path:
            grid[r][c] = '.'

# update S to be the kind of pipe it actually is
for r in range(0, len(grid)):
    for c in range(0, len(grid[0])):
        if grid[r][c] == 'S': # update S to be the kind of pipe it actually is
            if grid[r][c-1] in ['L', '-', 'F'] and grid[r+1][c] in ['|', 'J', 'L']:
                grid[r][c]= '7'
            elif grid[r][c-1] in ['L', '-', 'F'] and grid[r][c+1] in ['7', 'J', '-']:
                grid[r][c]= '-'
            elif grid[r-1][c] in ['|', '7', 'F'] and grid[r+1][c] in ['|', 'J', 'L']:
                grid[r][c]= '|'
            elif grid[r-1][c] in ['|', '7', 'F'] and grid[r][c-1] in ['L', '-', 'F']:
                grid[r][c]= 'J'
            elif grid[r][c+1] in ['7', 'J', '-'] and grid[r+1][c] in  ['|', 'J', 'L']:
                grid[r][c]= 'F'
            else:
                grid[r][c]= 'L'

# expand grid so all spots inside shape will be fillable
grid = expand_grid(grid)

# flood fill open spots. If a fill wasn't part of background (touched edge of grid) then 
# we're found the inside of the shape
done = False
for r in range(0, len(grid)):
    for c in range(0, len(grid[r])):
        if grid[r][c] == '.':
            spots, is_background = flood_fill(grid, r, c)
            if not is_background:
                done = True
                break
    if done:
        break

# add up total, without counting the new tiles we added
ans = 0
for r_idx, c_idx in spots:
    if r_idx % 2 == 0 and c_idx % 2 == 0: # not a new tile
        ans += 1
print(ans)
