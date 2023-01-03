from heapq import heappop, heappush
import math

grid = [list(row) for row in open('input.txt').read().split('\n')] 
SEARCH_DIRS = [(0,-1), (0,1), (-1,0), (1,0), (0,0)]  # (0, 0) for waiting
ARROWS = {'<': (0,-1), '>': (0,1), '^': (-1,0), 'v': (1,0)}
START = (0, grid[0].index('.'))  # row idx, col idx
END = (len(grid)-1, grid[-1].index('.'))
blizzards_memo = {}  # frozen set of current blizzards: frozen set of next blizzards


def blizzard_next_step(row_idx, col_idx, dir):
    row_change, col_change = ARROWS[dir]
    new_row_idx = row_idx + row_change
    new_col_idx = col_idx + col_change
    if grid[new_row_idx][new_col_idx] == '#':  # case where wrapping is needed
        if dir == '^':
            new_row_idx = len(grid)-2
        elif dir == 'v':
            new_row_idx = 1
        elif dir == '>':
            new_col_idx = 1
        elif dir == '<':
            new_col_idx = len(grid[0])-2
    return new_row_idx, new_col_idx, dir

# get our starting blizzards
blizzards = set()
for row_idx in range(0, len(grid)):
    for col_idx in range(0, len(grid[0])):
        if grid[row_idx][col_idx] in '><^v':
            blizzards.add((row_idx, col_idx, grid[row_idx][col_idx]))
            grid[row_idx][col_idx] = '.'  # grid is not for tracking blizzard position anymore
blizzards = frozenset(blizzards)

shortest_distances_from_start = {}  # (row_idx, col_idx): min dist (that we've found so far) from start to this vertex
# initialize distances to each vertex as inf, except for start vertex
for row_idx in range(0, len(grid)):
    for col_idx in range(0, len(grid[0])):
        shortest_distances_from_start[(row_idx, col_idx)] = math.inf
shortest_distances_from_start[START] = 0

# (dist, row_idx, col_idx, current blizzard locations, reached_end, reached_start)
# dist is first so that we're popping the vertex with min distance
priority_q = [(0, *START, blizzards, False, False)]
done = False
visited = set()
while priority_q and not done:
    popped = heappop(priority_q)
    if popped not in visited:
        visited.add(popped)
        curr_dist, curr_row, curr_col, blizzards, reached_end, reached_start = popped

        # get next blizzards
        if blizzards in blizzards_memo.keys():
            next_step_blizzards = blizzards_memo[blizzards]
        else:
            next_step_blizzards = set()
            for blizzard in blizzards:
                next_step_blizzards.add(blizzard_next_step(*blizzard))
            next_step_blizzards = frozenset(next_step_blizzards) 
            blizzards_memo[blizzards] = next_step_blizzards
        
        for row_change, col_change in SEARCH_DIRS:
            new_row = curr_row + row_change
            new_col = curr_col + col_change
            if (new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]) and
            grid[new_row][new_col] != '#' and 
            (new_row, new_col, '>') not in next_step_blizzards and (new_row, new_col, '<') not in next_step_blizzards and
            (new_row, new_col, '^') not in next_step_blizzards and (new_row, new_col, 'v') not in next_step_blizzards):
                if curr_dist + 1 <= shortest_distances_from_start[(new_row, new_col)]:
                    shortest_distances_from_start[(new_row, new_col)] = curr_dist + 1
                if (new_row, new_col) == END and reached_end is True and reached_start is True:
                    print(curr_dist+1)
                    done = True
                    break
                elif (new_row, new_col) == END and reached_end is False:
                    heappush(priority_q, (curr_dist + 1, new_row, new_col, next_step_blizzards, True, False)) 
                elif (new_row, new_col) == START and reached_end is True and reached_start is False:
                    heappush(priority_q, (curr_dist + 1, new_row, new_col, next_step_blizzards, True, True)) 
                else:
                    heappush(priority_q, (curr_dist + 1, new_row, new_col, next_step_blizzards, reached_end, reached_start))
