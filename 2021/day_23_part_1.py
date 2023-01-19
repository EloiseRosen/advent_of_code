from heapq import heappop, heappush
from collections import defaultdict
import math


# these 2 constants are the only difference between part 1 and part 2
ROOM_ROW_INDICES = [2, 3]
SHORT_ROWS_INDICES = [3, 4]  # the rows in the grid that are missing characters

COST_DCT = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
FINAL_COL_IDX_DCT = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
HALLWAY_ROW_IDX = 1
ROOM_COL_INDICES = FINAL_COL_IDX_DCT.values()

# populate final positions in a dict for convenience
FINAL_POS_DCT = {}
for row_idx in ROOM_ROW_INDICES:
    for col_idx in ROOM_COL_INDICES:
        pos = (row_idx, col_idx)
        for k, v in FINAL_COL_IDX_DCT.items():
            if v == col_idx:
                FINAL_POS_DCT[pos] = k
                break

# make the shorter rows the correct length to avoid index errors
grid = list(map(list, open('input.txt').read().split('\n')))
for short_row_idx in SHORT_ROWS_INDICES:
    grid[short_row_idx] = grid[short_row_idx] + [' ', ' ']

POSSIBLE_HALL_STOP_COL_INDICES = [i for i in range(1, len(grid[0])-1)]
for row_idx in ROOM_COL_INDICES:
    POSSIBLE_HALL_STOP_COL_INDICES.remove(row_idx)  # cannot stop right above a room

# pod_pos will be used to track our pod positions. Populate the initial places.
pod_pos = []  # (  ((row_idx, col_idx), 'A')  )
for row_idx in range(0, len(grid)):
    for col_idx in range(0, len(grid[0])):
        if grid[row_idx][col_idx] in 'ABCD':
            pod_pos.append(((row_idx, col_idx), grid[row_idx][col_idx]))
pod_pos = tuple(pod_pos)


def pod_finalized(pos, pod_pos):
    """A pod is finalized when it is in the correct room, and the pods below it are also
    in the correct room.
    """
    row_idx, col_idx = pos
    for idx in range(0, len(ROOM_ROW_INDICES)):
        room_row_idx = ROOM_ROW_INDICES[idx]
        if row_idx == room_row_idx:
            pod_in_right_room =  ((row_idx, col_idx) in FINAL_POS_DCT and 
                                  ((row_idx, col_idx), FINAL_POS_DCT[(row_idx, col_idx)]) in pod_pos)
            if not pod_in_right_room:
                return False

            for other_room_idx in range(idx+1, len(ROOM_ROW_INDICES)):
                other_room_row_idx = ROOM_ROW_INDICES[other_room_idx]
                if not pod_finalized((other_room_row_idx, col_idx), pod_pos):
                    return False
            return True
    return False


def get_cost(start_pos, end_pos, letter):
    start_row_idx, start_col_idx = start_pos
    end_row_idx, end_col_idx = end_pos
    spaces = abs(start_col_idx - end_col_idx)  # spaces in hall
    spaces += abs(HALLWAY_ROW_IDX - start_row_idx)  # spaces to exit room
    spaces += abs(HALLWAY_ROW_IDX - end_row_idx)  # spaces to enter room
    return spaces * COST_DCT[letter]


def blocked_in_hall(pos, end_col, pod_pos):
    start_row, start_col = pos
    for hall_col_idx in range(min(start_col, end_col), max(start_col, end_col)+1):
        for iter_pos, _ in pod_pos:
            if iter_pos == (HALLWAY_ROW_IDX, hall_col_idx) and iter_pos != pos:
                return True
    return False


def get_possible_moves(pos, pod_pos):
    if pod_finalized(pos, pod_pos):  # pod already in final resting place
        return []

    # are we in a room with a pod above us? if so, we can't move
    row_idx, col_idx = pos
    if row_idx in ROOM_ROW_INDICES:  # we're in a room, so have to check pods above us
        rooms_above_us_row_idx = [i for i in ROOM_ROW_INDICES if i < row_idx]
        for room_above_us_row_idx in rooms_above_us_row_idx:
            for iter_pos, _ in pod_pos:
                if iter_pos == (room_above_us_row_idx, col_idx):
                    return []

    # determine current letter for later use
    for iter_pos, iter_letter in pod_pos:
        if iter_pos == pos:
            letter = iter_letter
            break

    def get_final_dest(pos, letter, pod_pos):
        """Returns (additional cost, (row_idx, col_idx)) of final destination if move to 
        final destination is currently possible, None otherwise"""
        final_dest_col = FINAL_COL_IDX_DCT[letter]

        # does final destination room have un-finalized pods in it?
        for (iter_row, iter_col), iter_letter in pod_pos:
            if (iter_col == final_dest_col and iter_row in ROOM_ROW_INDICES
            and not pod_finalized((iter_row, iter_col), pod_pos)):
                return None

        if blocked_in_hall(pos, final_dest_col, pod_pos):
            return None

        # If we're still here, we can move into final room!
        # the pod goes to the lowest empty level
        found_pod = False
        for room_idx in ROOM_ROW_INDICES:  # starting from top-most
            for iter_pos, _ in pod_pos:
                if iter_pos == (room_idx, final_dest_col):
                    final_dest_row = room_idx - 1
                    found_pod = True
                    break
            if found_pod:
                break
        if not found_pod:
            final_dest_row = max(ROOM_ROW_INDICES)  # no pods in room so go to lowest space

        additional_cost = get_cost(pos, (final_dest_row, final_dest_col), letter)
        return additional_cost, (final_dest_row, final_dest_col)

    def get_hall_moves(pos, letter, pod_pos):
        row_idx, col_idx = pos
        if row_idx == HALLWAY_ROW_IDX:
            return []
        rtn = []
        for possible_col in POSSIBLE_HALL_STOP_COL_INDICES:
            if not blocked_in_hall(pos, possible_col, pod_pos):
                additional_cost = get_cost(pos, (HALLWAY_ROW_IDX, possible_col), letter)
                rtn.append((additional_cost, (HALLWAY_ROW_IDX, possible_col)))
        return rtn

    possible_moves = []  # [  (additional_cost, (new_row_idx, new_col_idx))  ]
    final_dest = get_final_dest(pos, letter, pod_pos)
    if final_dest is not None:
        possible_moves.append(final_dest)
    possible_moves.extend(get_hall_moves(pos, letter, pod_pos))
    return possible_moves


def all_pods_organized(pod_pos):
    for (row_idx, col_idx), letter in pod_pos:
        if row_idx not in ROOM_ROW_INDICES or FINAL_COL_IDX_DCT[letter] != col_idx:
            return False
    return True


# {pod_pos: min cost (that we've found so far) from start to here}
least_cost_from_start = defaultdict(lambda: math.inf)
least_cost_from_start[tuple(sorted(pod_pos))] = 0

# initially populate priority_q
priority_q = []  # (cost, pod_pos). cost is first so that we're popping based on min cost
for pos, letter in pod_pos:
    possible_moves = get_possible_moves(pos, pod_pos)
    for cost, new_pos in possible_moves:
        # move pod to new location
        new_pod_pos = []
        for iter_pos, iter_letter in pod_pos:
            if iter_pos == pos:
                new_pod_pos.append((new_pos, letter))
            else:
                new_pod_pos.append((iter_pos, iter_letter))
        new_pod_pos = tuple(new_pod_pos)

        least_cost_from_start[tuple(sorted(new_pod_pos))] = cost
        
        heappush(priority_q, (cost, tuple(sorted(new_pod_pos))))


visited = set()
while priority_q:
    cost, pod_pos = heappop(priority_q)

    # Ugh end check has to be here right after popping from heap so that it's for sure the
    # min: if end check is later in loop when cost is previous cost + additional cost then
    # there may be cheaper paths still on the heap.
    if all_pods_organized(pod_pos):
        print(cost)
        break

    if pod_pos not in visited:
        visited.add(tuple(sorted(pod_pos)))

        for pos, letter in pod_pos:
            possible_moves = get_possible_moves(pos, pod_pos)
            for new_cost, new_pos in possible_moves:
                # move pod to new location
                new_pod_pos = []
                for iter_pos, iter_letter in pod_pos:
                    if iter_pos == pos:
                        new_pod_pos.append((new_pos, letter))
                    else:
                        new_pod_pos.append((iter_pos, iter_letter))
                new_pod_pos = tuple(new_pod_pos)
                if cost+new_cost <= least_cost_from_start[tuple(sorted(new_pod_pos))]:
                    least_cost_from_start[tuple(sorted(new_pod_pos))] = cost+new_cost

                heappush(priority_q, (cost+new_cost, tuple(sorted(new_pod_pos))))
