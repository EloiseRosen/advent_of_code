ans = 0
grid = list(map(list, open('input.txt').read().split('\n')))
for c_idx in range(0, len(grid[0])):
    last_immovable = -1
    round_since_last_immovable = 0
    for r_idx in range(0, len(grid)):
        if grid[r_idx][c_idx] == '#':
            last_immovable = r_idx
            round_since_last_immovable = 0
        elif grid[r_idx][c_idx] == 'O':
            ans += len(grid) - ((last_immovable+1) + round_since_last_immovable)
            round_since_last_immovable += 1
print(ans)
