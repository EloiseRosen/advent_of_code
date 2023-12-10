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

# calculate furthest point by steps
print((len(path)-1)/2)
