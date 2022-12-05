crates, moves = open('input.txt').read().split('\n\n')
crates = crates.split('\n')[:-1]
moves = moves.split('\n')
num_crates = (len(crates[0])+1)//4

stacks = [[] for _ in range(0, num_crates)]
for crate_line in crates:
    for crate_line_idx in range(1, len(crates[0]), 4):
        box = crate_line[crate_line_idx]
        if box != ' ':
            stack_idx = (crate_line_idx-1)//4
            stacks[stack_idx].insert(0, box)

for move in moves:
    move_lst = move.split(' ')
    num_items_to_move = int(move_lst[1])
    start = int(move_lst[3])
    end = int(move_lst[5])
    boxes = stacks[start-1][-num_items_to_move:]
    stacks[start-1] = stacks[start-1][:-num_items_to_move]
    stacks[end-1].extend(boxes)

tops = []
for stack in stacks:
    tops.append(stack[-1])
print(''.join(tops))
