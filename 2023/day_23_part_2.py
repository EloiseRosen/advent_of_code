DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
GRID = [list(r) for r in open('input.txt').read().split('\n')]
START = (0, GRID[0].index('.'))
END = (len(GRID)-1, GRID[len(GRID)-1].index('.'))


def get_decision_points(GRID, DIRS):
    def is_decision_point(r, c, DIRS):
        if GRID[r][c] != '.':
            return False
        slope_count = 0 # note that in input, the decision points are the ones with slopes around them
        for r_change, c_change in DIRS:
            new_r = r + r_change
            new_c = c + c_change
            if (new_r >= 0 and new_r < len(GRID) and new_c >= 0 and new_c < len(GRID[0])):
                if GRID[new_r][new_c] == '.':
                    return False
                if GRID[new_r][new_c] in '^v<>':
                    slope_count += 1
        return slope_count >= 2
    
    decision_points = set()
    for r in range(0, len(GRID)):
        for c in range(0, len(GRID[0])-1):
            if is_decision_point(r, c, DIRS):
                decision_points.add( (r, c) )
    decision_points.add(START)
    decision_points.add(END)
    return decision_points


def get_connections(decision_points, GRID, DIRS):
    connections = {dp: [] for dp in decision_points}  # decision_point: [((r, c), dist), ((r, c), dist)]
    connections[START] = []
    connections[END] = []
    for dp in decision_points:  # find what it's connected to, and how far away
        stack = [(dp, set())]  # [((r, c), seen)]
        while stack:
            (r, c), seen = stack.pop()
            new_seen = seen.copy()
            new_seen.add( (r, c) )

            if (r, c) in decision_points and (r, c) != dp:
                connections[(dp)].append( ((r, c), len(new_seen)-1) )
            else:
                for r_change, c_change in DIRS:
                    new_r = r + r_change
                    new_c = c + c_change
                    if (new_r >= 0 and new_r < len(GRID) and new_c >= 0 and new_c < len(GRID[0]) and
                    GRID[new_r][new_c] in '.><^v' and (new_r, new_c) not in new_seen):
                        stack.append( ((new_r, new_c), new_seen) )
    return connections


decision_points = sorted(get_decision_points(GRID, DIRS))
connections = get_connections(decision_points, GRID, DIRS)

max_length = 0
stack = [(START, set(), 0)]  # [((r, c), seen, number steps)]
while stack:
    (r, c), seen, total_num_steps = stack.pop()
    new_seen = seen.copy()
    new_seen.add( (r, c) )

    if (r, c) == END:
        max_length = max(max_length, total_num_steps)
    else:
        for (connection_r, connection_c), num_steps in connections[(r, c)]:
            if (connection_r, connection_c) not in new_seen:
                stack.append( ((connection_r, connection_c), new_seen, total_num_steps+num_steps) )

print(max_length)
