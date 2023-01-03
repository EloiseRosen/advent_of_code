from collections import defaultdict

grid = [list(row) for row in open('input.txt').read().split('\n')]
elves_lst = []  # each elf will always be located at the same index
for row_idx in range(0, len(grid)):
    for col_idx in range(0, len(grid[0])):
        if grid[row_idx][col_idx] == '#':
            elves_lst.append((row_idx, col_idx))


proposal_dirs = [
    [(-1,0), (-1,-1), (-1,1)], 
    [(1,0), (1,-1), (1,1)],
    [(0,-1), (1,-1), (-1,-1)],
    [(0,1), (1,1), (-1,1)]
]
def get_proposal(elf_row, elf_col, elves, proposal_dirs):
    for proposal_dir in proposal_dirs:
        final_row_change, final_col_change = proposal_dir[0]
        can_move_this_direction = True
        for row_change, col_change in proposal_dir:
            new_row = elf_row + row_change
            new_col = elf_col + col_change
            if (new_row, new_col) in elves:
                can_move_this_direction = False
                break
        if can_move_this_direction:
            return (elf_row + final_row_change, elf_col + final_col_change)
    return None


DIRS = [(0,-1), (0,1), (-1,0), (1,0), (-1,-1), (1,1), (-1,1), (1,-1)]
round = 1
while True:
    original_elves_lst = elves_lst[:]
    # During the first half of each round, each Elf considers the eight positions adjacent to themself.
    proposal_by_idx = []
    proposal_count_dct = defaultdict(lambda: 0)
    for elf_row, elf_col in elves_lst:
        surrounding_elves = False
        for row_change, col_change in DIRS:
            new_row = elf_row + row_change
            new_col  = elf_col + col_change
            if (new_row, new_col) in elves_lst:
                surrounding_elves = True
                break

        if surrounding_elves:
            proposal = get_proposal(elf_row, elf_col, elves_lst, proposal_dirs)
            proposal_by_idx.append(proposal)
            if proposal is not None:
                proposal_count_dct[proposal] += 1
        else:
            proposal_by_idx.append(None)

    # After each Elf has had a chance to propose a move, the second half of the round can begin. Simultaneously, 
    # each Elf moves to their proposed destination tile if they were the only Elf to propose moving to that position. 
    # If two or more Elves propose moving to the same position, none of those Elves move.
    for idx, (elf_row, elf_col) in enumerate(elves_lst):
        proposal = proposal_by_idx[idx]
        if proposal is not None and proposal_count_dct[proposal] == 1:
            elves_lst[idx] = proposal

    # Finally, at the end of the round, the first direction the Elves considered is moved to the end of the list 
    to_move = proposal_dirs.pop(0)
    proposal_dirs.append(to_move)

    if original_elves_lst == elves_lst:
        break
    round += 1

print(round)
