trees = [[int(el) for el in list(row)] for row in open('input.txt').read().split('\n')]
visible = set()

for row_idx in range(0, len(trees)):
    max_height = None
    for col_idx in range(0, len(trees[0])):  # rows from left
        if max_height is None or trees[row_idx][col_idx] > max_height:
            visible.add((row_idx, col_idx))
            max_height = trees[row_idx][col_idx]
    max_height = None
    for col_idx in range(len(trees[0])-1, -1, -1):  # rows from right
        if max_height is None or trees[row_idx][col_idx] > max_height:
            visible.add((row_idx, col_idx))
            max_height = trees[row_idx][col_idx]
    max_height = None
for col_idx in range(0, len(trees[0])):
    max_height = None
    for row_idx in range(0, len(trees)):  # cols from up
        if max_height is None or trees[row_idx][col_idx] > max_height:
            visible.add((row_idx, col_idx))
            max_height = trees[row_idx][col_idx]
    max_height = None
    for row_idx in range(len(trees)-1, -1, -1):  # cols from down
        if max_height is None or trees[row_idx][col_idx] > max_height:
            visible.add((row_idx, col_idx))
            max_height = trees[row_idx][col_idx]
    max_height = None

print(len(visible))
