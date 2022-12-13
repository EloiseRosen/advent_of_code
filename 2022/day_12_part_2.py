# for part 2, go from 'E' to the first 'a'
from collections import deque

grid = [list(line) for line in open('input.txt').read().split('\n')]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(grid):
    for row_idx in range(0, len(grid)):
        if 'S' in grid[row_idx]:
            col_idx = grid[row_idx].index('S')
            grid[row_idx][col_idx] = 'a'
        if 'E' in grid[row_idx]:
            col_idx = grid[row_idx].index('E')
            start = (row_idx, col_idx)
            grid[row_idx][col_idx] = 'z'

    visited = {start}
    q = deque([[start]])
    while q:
        path = q.popleft()
        row_idx, col_idx = path[-1]
        for row_change, col_change in dirs:
            new_row_idx = row_idx + row_change
            new_col_idx = col_idx + col_change
            if (new_row_idx >= 0 and new_row_idx < len(grid) 
            and new_col_idx >= 0 and new_col_idx < len(grid[0]) 
            and (new_row_idx, new_col_idx) not in visited
            and ord(grid[row_idx][col_idx]) - ord(grid[new_row_idx][new_col_idx]) <= 1):
                new_path = path + [(new_row_idx, new_col_idx)]
                if grid[new_row_idx][new_col_idx] == 'a':
                    return len(new_path) - 1  # -1 bc we're counting the # of movements, not positions
                visited.add((new_row_idx, new_col_idx))
                q.append(new_path)

print(bfs(grid))
