from heapq import heappop, heappush
import math

grid = [list(map(int, list(row))) for row in open('input.txt').read().split('\n')]

START = (0, 0)
END = (len(grid)-1, len(grid[0])-1)
DIRS = [(0,-1), (0,1), (-1,0), (1,0), (0,0)]

shortest_distances_from_start = {}  # (row_idx, col_idx): min dist (that we've found so far) from start to this vertex
# initialize distances to each vertex as inf, except for start vertex
for row_idx in range(0, len(grid)):
    for col_idx in range(0, len(grid[0])):
        shortest_distances_from_start[(row_idx, col_idx)] = math.inf
shortest_distances_from_start[START] = 0

# (dist, row_idx, col_idx). dist is first so that we're popping the vertex with min distance
priority_q = [(0, *START)]
done = False
visited = set()
while priority_q and not done:
    curr_dist, curr_row, curr_col = heappop(priority_q)
    if (curr_row, curr_col) not in visited:
        visited.add((curr_row, curr_col))

        for row_change, col_change in DIRS:
            new_row = curr_row + row_change
            new_col = curr_col + col_change
            if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
                new_total_dist = curr_dist + grid[new_row][new_col] 
                if new_total_dist <= shortest_distances_from_start[(new_row, new_col)]:
                    shortest_distances_from_start[(new_row, new_col)] = new_total_dist
                if (new_row, new_col) == END:
                    done = True
                    break
                heappush(priority_q, (new_total_dist, new_row, new_col))

print(shortest_distances_from_start[END])
