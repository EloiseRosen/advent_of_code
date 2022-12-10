lst = [row.split(' ') for row in open('input.txt').read().split('\n')]

non_diag_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
diag_dirs = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
head = [0, 0]
tail = [0, 0]
visited = {(0, 0)} 


def is_touching(head, tail):
    return abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1


def get_new_positions(move_head_dir, head, tail):
    new_head = head[:]
    new_tail = tail[:]
    if move_head_dir == 'R':
        new_head[1] += 1
    elif move_head_dir == 'L':
        new_head[1] -= 1
    elif move_head_dir == 'U':
        new_head[0] -= 1
    elif move_head_dir == 'D':
        new_head[0] += 1

    # catch up tail
    if not is_touching(new_head, new_tail):
        dirs = non_diag_dirs if (new_head[0] == new_tail[0] or new_head[1] == new_tail[1]) else diag_dirs
        for row_change, col_change in dirs:
            new_tail = [tail[0]+row_change, tail[1]+col_change]
            if is_touching(new_head, new_tail):
                return new_head, new_tail
    return new_head, new_tail
    

for dir, dist in lst:
    for _ in range(0, int(dist)):
        head, tail = get_new_positions(dir, head, tail)
        visited.add(tuple(tail))

print(len(visited))
