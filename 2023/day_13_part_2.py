def vertical_reflection(grid):
    for idx in range(0, len(grid)-1):
        errors = 0
        for offset_iteration in range(-1, min(idx, len(grid)-idx-2)):
            offset = offset_iteration + 1
            for el1, el2 in zip(grid[idx-offset], grid[idx+1+offset]):
                if el1 != el2:
                    errors += 1
        if errors == 1:
            return idx + 1
    return -1


ans = 0
for grid in open('input.txt').read().split('\n\n'):
    grid = grid.split('\n')

    if (vert := vertical_reflection(grid)) != -1:
        ans += vert * 100

    rotated_grid = [list(col[::-1]) for col in zip(*grid)]
    if (horiz := vertical_reflection(rotated_grid)) != -1:
        ans += horiz

print(ans)
