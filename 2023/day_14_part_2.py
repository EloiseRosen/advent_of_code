CYCLES = 1_000_000_000


def do_cycle(grid):
    for _ in range(0, 4):
        for c_idx in range(0, len(grid[0])):
            last_immovable = -1
            round_since_last_immovable = 0
            for r_idx in range(0, len(grid)):
                if grid[r_idx][c_idx] == '#':
                    last_immovable = r_idx
                    round_since_last_immovable = 0
                elif grid[r_idx][c_idx] == 'O':
                    new_location = (last_immovable+1) + round_since_last_immovable
                    grid[r_idx][c_idx] = '.'
                    grid[new_location][c_idx] = 'O'
                    round_since_last_immovable += 1
        grid = [list(col[::-1]) for col in zip(*grid)]
    return grid


def get_load(grid):
    rtn = 0
    for c_idx in range(0, len(grid[0])):
        for r_idx in range(0, len(grid)):
            if grid[r_idx][c_idx] == 'O':
                rtn += len(grid) - r_idx
    return rtn


grid = list(map(list, open('input.txt').read().split('\n')))

# get length of tail + loop
seen = set()
while (immutable_grid := tuple((tuple(row) for row in grid))) not in seen:
    seen.add(immutable_grid)
    grid = do_cycle(grid)
tail_and_loop = len(seen)

# get length of tail
for _ in range(0, tail_and_loop):
    immutable_grid = tuple((tuple(row) for row in grid))
    seen.discard(immutable_grid)
    grid = do_cycle(grid)
tail = len(seen)

# get final state
loop = tail_and_loop - tail
end_this_many_into_cycle = (CYCLES - tail) % loop
new_cycles = tail + end_this_many_into_cycle
grid = list(map(list, open('input.txt').read().split('\n')))
for _ in range(0, new_cycles):
    grid = do_cycle(grid)
print(get_load(grid))
