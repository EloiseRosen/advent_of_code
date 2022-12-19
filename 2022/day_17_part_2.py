from itertools import cycle

NUM_ROCK_DROPS = 1000000000000
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


def get_empty_heights(set_of_points):
    empty_heights = [None for col in range(0, WIDTH)]
    for col_idx in range(0, WIDTH):
        row_idx = 0
        while (row_idx, col_idx) not in set_of_points:
            row_idx += 1
        empty_heights[col_idx] = row_idx
    return empty_heights


rocks = cycle(ROCKS)
moves = cycle(lst)
iteration = 0
start_cycle_check = 1000
check_cycle = False
while iteration < NUM_ROCK_DROPS:
    original_rock, height = next(rocks)
    rock = original_rock.copy()
    # shift the other points down to accomodate the height of the rock
    full = {(row+height, col) for row, col in full}
        
    # get a snapshot of the current state
    if iteration == start_cycle_check:
        empty_heights = get_empty_heights(full)
        snapshot_state = tuple(empty_heights) + tuple(rock) + tuple(move)
        check_cycle = True
        start_height = max(full, key=lambda x: x[0])[0] - min(full, key=lambda x: x[0])[0]
    # when do we next reach the same state? how much height did we add in the interim?
    if check_cycle and iteration != start_cycle_check:
        empty_heights = get_empty_heights(full)
        curr_state = tuple(empty_heights) + tuple(rock) + tuple(move)
        if curr_state == snapshot_state:
            curr_height = max(full, key=lambda x: x[0])[0] - min(full, key=lambda x: x[0])[0]
            cycle_height = curr_height - start_height
            cycle_length = iteration - start_cycle_check
            num_cycles, remainder = divmod(NUM_ROCK_DROPS-start_cycle_check, cycle_length)
            # finish up the last days at the end that don't fit neatly in a cycle
            iteration = NUM_ROCK_DROPS - remainder

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
    iteration += 1

start_and_remainder_height = max(full, key=lambda x: x[0])[0] - min(full, key=lambda x: x[0])[0]
final_ans = start_and_remainder_height + (num_cycles-1)*cycle_height
print(final_ans)
