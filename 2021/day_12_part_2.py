lst = open('input.txt').read().split('\n')

dct = {}
for line in lst:
    start, end = line.split('-')
    dct[start] = {end} if start not in dct else dct[start] | {end}
    dct[end] = {start} if end not in dct else dct[end] | {start}

final_paths = []
stack = []  # (curr_pos, path, double_is_done)
for val in dct['start']:
    stack.append((val, ['start'], False))
while stack:
    curr_pos, path, double_done = stack.pop()
    if curr_pos == 'end':
        path.append('end')
        final_paths.append(path)
    elif curr_pos.isupper():
        path.append(curr_pos)
        for val in dct[curr_pos]:
            stack.append((val, path[:], double_done))
    elif curr_pos.islower() and curr_pos != 'start':
        if curr_pos not in path:
            path.append(curr_pos)
            for val in dct[curr_pos]:
                stack.append((val, path[:], double_done))
        elif path.count(curr_pos) == 1 and not double_done:
            path.append(curr_pos)
            for val in dct[curr_pos]:
                stack.append((val, path[:], True))

print(len(final_paths))
