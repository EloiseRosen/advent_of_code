def vertical_reflection(grid):
    for idx in range(0, len(grid)-1):
        if grid[idx] == grid[idx+1]:
            is_reflection = True
            for offset_iteration in range(0, min(idx, len(grid)-idx-2)):
                offset = offset_iteration + 1
                if grid[idx-offset] != grid[idx+1+offset]:
                    is_reflection = False
                    break
            if is_reflection:
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
