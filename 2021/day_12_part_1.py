lst = open('input.txt').read().split('\n')

dct = {}
for line in lst:
    start, end = line.split('-')
    dct[start] = {end} if start not in dct else dct[start] | {end}
    dct[end] = {start} if end not in dct else dct[end] | {start}

final_paths = []
stack = []  # (curr_pos, path)
for val in dct['start']:
    stack.append((val, ['start']))
while stack:
    curr_pos, path = stack.pop()
    if curr_pos == 'end':
        path.append('end')
        final_paths.append(path)
    elif curr_pos.isupper():
        path.append(curr_pos)
        for val in dct[curr_pos]:
            stack.append((val, path[:]))
    elif curr_pos.islower() and curr_pos != 'start':
        if curr_pos not in path:
            path.append(curr_pos)
            for val in dct[curr_pos]:
                stack.append((val, path[:]))

print(len(final_paths))
