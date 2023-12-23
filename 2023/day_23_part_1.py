DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
SLOPES = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
GRID = [list(r) for r in open('input.txt').read().split('\n')]
START = (0, GRID[0].index('.'))
END = (len(GRID)-1, GRID[len(GRID)-1].index('.'))


max_length = 0
stack = [(START, set())]  # [((r, c), seen)]
while stack:
    (r, c), seen = stack.pop()
    new_seen = seen.copy()
    new_seen.add( (r, c) )

    if (r, c) == END:
        max_length = max(max_length, len(new_seen)-1)

    for r_change, c_change in DIRS:
        new_r = r + r_change
        new_c = c + c_change
        if (new_r >= 0 and new_r < len(GRID) and new_c >= 0 and new_c < len(GRID[0]) and
        GRID[new_r][new_c] in '.><^v' and (new_r, new_c) not in new_seen):
            if GRID[r][c] in SLOPES: # if we're on slope, only add to stack if we're doing the allowed move
                if (r_change, c_change) == SLOPES[GRID[r][c]]:
                    stack.append( ((new_r, new_c), new_seen) )
            else:
                stack.append( ((new_r, new_c), new_seen) )

print(max_length)
