MOVE = {'>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)}

REFLECT = {('/', 0, 1): '^',
           ('/', 0, -1): 'v',
           ('/', -1, 0): '>',
           ('/', 1, 0): '<',
           ('\\', 0, 1): 'v',
           ('\\', 0, -1): '^',
           ('\\', -1, 0): '<',
           ('\\', 1, 0): '>'}

SPLIT = {('|', 0, 1): ['^', 'v'],
         ('|', 0, -1): ['^', 'v'],
         ('-', -1, 0):  ['<', '>'],
         ('-', 1, 0):  ['<', '>']}


def run(start):
    seen = set() # (direction, row index, col index)
    curr_points = {start}
    energized = set()
    while curr_points:
        new_curr_points = set()
        for curr_dir, r, c in curr_points:
            if (curr_dir, r, c) not in seen: # if seen we can stop simulating this beam
                seen.add( (curr_dir, r, c) )
                energized.add( (r, c) )
                r_change, c_change = MOVE[curr_dir]
                new_r = r + r_change
                new_c = c + c_change
                if new_r >= 0 and new_r < len(grid) and new_c >= 0 and new_c < len(grid[0]):
                    if (grid[new_r][new_c], r_change, c_change) in REFLECT:
                        new_curr_points.add( (REFLECT[(grid[new_r][new_c], r_change, c_change)], new_r, new_c) )
                    elif (grid[new_r][new_c], r_change, c_change) in SPLIT:
                        for new_dir in SPLIT[(grid[new_r][new_c], r_change, c_change)]:
                            new_curr_points.add( (new_dir, new_r, new_c) )
                    else:
                        new_curr_points.add( (curr_dir, new_r, new_c) )
        curr_points = new_curr_points
    return len(energized) - 1 # -1 because the off-screen start doesn't count


grid = open('input.txt').read().split('\n')
ans = 0
for c in range(0, len(grid[0])):
    ans = max(ans, run( ('v', -1, c) ))  # start at the top going down
    ans = max(ans, run( ('^', len(grid), c) ))  # start at the bottom going up
for r in range(0, len(grid)):
    ans = max(ans, run( ('>', r, -1) ))  # start at the left going right
    ans = max(ans, run( ('<', r, len(grid[0])) ))  # start at the right going left
print(ans)
