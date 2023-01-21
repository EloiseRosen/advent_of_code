grid = open('input.txt').read().split('\n')
HEIGHT = len(grid)
WIDTH = len(grid[0])


def get_next_pos(pos, symbol):
    row_idx, col_idx = pos
    if symbol == '>':
        col_idx += 1
    if symbol == 'v':
        row_idx += 1
    if row_idx >= HEIGHT:
        row_idx = 0
    if col_idx >= WIDTH:
        col_idx = 0
    return row_idx, col_idx
    

def move_cucumber_group(old_move_set, other_set):
    changed = False
    occupied_set = old_move_set | other_set
    new_set = set()
    for pos, symbol in old_move_set:
        new_pos = get_next_pos(pos, symbol)
        if (new_pos, '>') in occupied_set or (new_pos, 'v') in occupied_set:
            new_set.add(((pos), symbol))
        else:
            new_set.add(((new_pos), symbol))
            changed = True
    return new_set, changed


east = set()
south = set()
for row_idx in range(0, HEIGHT):
    for col_idx in range(0, WIDTH):
        if grid[row_idx][col_idx] == '>':
            east.add(((row_idx, col_idx), '>'))
        elif grid[row_idx][col_idx] == 'v':
            south.add(((row_idx, col_idx), 'v'))

step = 1
while True:
    new_east, east_changed = move_cucumber_group(east, south)
    new_south, south_changed = move_cucumber_group(south, new_east)
    if not east_changed and not south_changed: 
        print(step)
        break

    east = new_east
    south = new_south
    step += 1
