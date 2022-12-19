from itertools import cycle

NUM_ROCK_DROPS = 2022
WIDTH = 7
EMPTY_SPACE_HEIGHT = 3
ROCKS = (  # set of rock points, height
    ({(0,2), (0,3), (0,4), (0,5)}, 1),
    #[['.', '.', '#', '#', '#', '#', '.']],

    ({(0,3), (1,2), (1,3), (1,4), (2,3)}, 3),
    # [['.', '.', '.', '#', '.', '.', '.'],
    #  ['.', '.', '#', '#', '#', '.', '.'],
    #  ['.', '.', '.', '#', '.', '.', '.']],

    ({(0,4), (1,4), (2,2), (2,3), (2,4)}, 3),
    # [['.', '.', '.', '.', '#', '.', '.'],
    #  ['.', '.', '.', '.', '#', '.', '.'],
    #  ['.', '.', '#', '#', '#', '.', '.']],

    ({(0,2), (1,2), (2,2), (3,2)}, 4),
    # [['.', '.', '#', '.', '.', '.', '.'],
    #  ['.', '.', '#', '.', '.', '.', '.'],
    #  ['.', '.', '#', '.', '.', '.', '.'],
    #  ['.', '.', '#', '.', '.', '.', '.']],

    ({(0,2), (0,3), (1,2), (1,3)}, 2),
    # [['.', '.', '#', '#', '.', '.', '.'],
    #  ['.', '.', '#', '#', '.', '.', '.']]
)


lst = [char for char in open('input.txt').read()]

 # treat the floor as settled tetris pieces, remove 1 from height at end
floor_row = max(ROCKS[0][0], key=lambda x: x[0])[0] + EMPTY_SPACE_HEIGHT
full = {(floor_row, col) for col in range(0, WIDTH)}


def move_horizontal(original_rock, full, move_right):
    new_rock = set()
    for row, col in original_rock:
        if move_right:
            new_col = col + 1
        else:
            new_col = col - 1
        if new_col < 0 or new_col == WIDTH or (row, new_col) in full:
            return original_rock
        new_rock.add((row, new_col))
    return new_rock


def move_down(original_rock, original_full):
    """Returns updated set, and boolean indicating if move was possible"""
    add_one = False
    new_full = set()
    # moving the rock down 1 is like moving the rest up 1
    for row, col in original_full:
        if (row-1, col) in original_rock:
            return original_rock, original_full, False
        new_full.add((row-1, col))
        if row-1 < 0:
            add_one = True

    if add_one:
        rock_add_one = {(row+1, col) for (row, col) in original_rock}
        new_full_add_one = {(row+1, col) for (row, col) in new_full}
        return rock_add_one, new_full_add_one, True
    else:
        return original_rock, new_full, True


rocks = cycle(ROCKS)
moves = cycle(lst)
for iteration in range(0, NUM_ROCK_DROPS):
    original_rock, height = next(rocks)
    rock = original_rock.copy()
    # shift the other points down to accomodate the height of the rock
    full = {(row+height, col) for row, col in full}

    move_down_was_possible = True
    while move_down_was_possible:
        # move horizontal
        move = next(moves)
        if move == '>':
            rock = move_horizontal(rock, full, move_right=True)
        elif move == '<':
            rock = move_horizontal(rock, full, move_right=False)
            
        # move down
        rock, full, move_down_was_possible = move_down(rock, full)

    # prepare for next iteration: each rock appears so that its bottom edge 
    # is EMPTY_SPACE_HEIGHT above the highest rock.
    full |= rock
    full = {(row+EMPTY_SPACE_HEIGHT, col) for row, col in full}

min_row = None
max_row = None
for row, col in full:
    if min_row is None or row < min_row:
        min_row = row
    if max_row is None or row > max_row:
        max_row = row
print(max_row - min_row)
