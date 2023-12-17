import heapq


grid = [list(map(int, r)) for r in open('input.txt').read().split('\n')]
DIRS =  [(0, 1), (0, -1), (1, 0), (-1, 0)]
START = (0, 0)
END = (len(grid)-1, len(grid[0])-1)
MAX_STEPS_IN_DIR = 3

seen = set()
# "Because you already start in the top-left block, you don't incur that block's heat 
# loss unless you leave that block and then return to it."
min_heap = [(0, 0,0, 0,0, 0)] # cost, r,c, last_r_change,last_c_change, consecutive_steps_in_dir
while min_heap:
    cost, r,c, last_r_change,last_c_change, steps_in_dir = heapq.heappop(min_heap)
    if (r,c, last_r_change,last_c_change, steps_in_dir) not in seen:
        seen.add((r,c, last_r_change,last_c_change, steps_in_dir))

        if (r, c) == END:
            print(cost)
            break

        for r_change, c_change in DIRS:
            new_r = r + r_change
            new_c = c + c_change
            if (new_r >= 0 and new_r < len(grid) and new_c >= 0 and new_c < len(grid[0]) and  # in bounds
                (last_r_change*-1, last_c_change*-1) != (r_change, c_change) and  # can't reverse direction
                (steps_in_dir < MAX_STEPS_IN_DIR or (last_r_change, last_c_change) != (r_change, c_change))):  # can't move in same dir more than 3 times
                    new_cost = cost + grid[new_r][new_c]

                    if last_r_change == r_change and last_c_change == c_change:
                        new_steps_in_dir = steps_in_dir+1
                    else:
                        new_steps_in_dir = 1

                    heapq.heappush(min_heap, (new_cost, new_r,new_c, r_change,c_change, new_steps_in_dir))
