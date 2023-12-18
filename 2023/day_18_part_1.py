def flood_fill(edge, sr, sc):
    seen = set()
    stack = [(sr, sc)]
    while stack:
        r, c = stack.pop()
        if (r, c) not in seen and (r, c) not in edge:
            seen.add((r, c))
            for r_change, c_change in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r = r + r_change
                new_c = c + c_change
                stack.append((new_r, new_c))
    return len(seen)


edge = {(0, 0)}
r, c = 0, 0
for line in open('input.txt').read().split('\n'):
    dir_, amount, _ = line.split(' ')
    amount = int(amount)
    for _ in range(0, amount):
        if dir_ == 'R':
            c += 1
        if dir_ == 'L':
            c -= 1
        if dir_ == 'U':
            r -= 1
        if dir_ == 'D':
            r += 1
        edge.add( (r, c) )

print(flood_fill(edge, -1, 0) + len(edge))
