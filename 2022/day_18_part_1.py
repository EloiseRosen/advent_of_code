points = {tuple(map(int, row.split(','))) for row in open('input.txt').read().split('\n')}
dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

ans = 0
for x, y, z in points:
    for x_change, y_change, z_change in dirs:
        new_x = x + x_change
        new_y = y + y_change
        new_z = z + z_change
        if (new_x, new_y, new_z) not in points:
            ans += 1

print(ans)
