DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
STEPS = 64
GRID = [list(line) for line in open('input.txt').read().split('\n')]


def dfs(GRID, DIRS, STEPS):
    # get start
    for r in range(0, len(GRID)):
        for c in range(0, len(GRID[0])):
            if GRID[r][c] == 'S':
                start = (r, c)

    # entries are (r, c, steps). We can double back, but if we're at the same spot with
    # the same number of steps we can stop.
    seen = set()

    stack = [(start[0], start[1], 0)]  # (r, c, steps)
    all_final_spots = set()

    while stack:
        r, c, steps = stack.pop()
        seen.add( (r, c, steps) )

        if steps == STEPS:
            all_final_spots.add( (r, c) )
        else:
            for r_change, c_change in DIRS:
                new_r = r + r_change
                new_c = c + c_change
                if (new_r >= 0 and new_r < len(GRID) and new_c >= 0 and new_c < len(GRID[0])
                    and GRID[new_r][new_c] != '#' and (new_r, new_c, steps+1) not in seen):
                    stack.append( (new_r, new_c, steps+1) )
    return all_final_spots


all_final_spots = dfs(GRID, DIRS, STEPS)
print(len(all_final_spots))
