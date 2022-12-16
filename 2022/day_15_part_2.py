from collections import defaultdict

MAX_ROW = 4_000_000
MAX_COL = 4_000_000
sensor_lst = [line.split(': ') for line in open('input.txt').read().split('\n')]


def manhattan_dist(row1, col1, row2, col2):
    return abs(row1 - row2) + abs(col1 - col2)


# get the points that are 1 beyond the area of a sensor
points_one_beyond_perimeter = defaultdict(lambda: 0)
mult = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
for idx, line in enumerate(sensor_lst):
    sensor, beacon = line
    sensor_col, sensor_row = map(int, sensor[len('Sensor at x='):].split(', y='))
    beacon_col, beacon_row = map(int, beacon[len('closest beacon is at x='):].split(', y='))
    beacon_dist = manhattan_dist(sensor_row, sensor_col, beacon_row, beacon_col)
    sensor_lst[idx] = ((sensor_row, sensor_col), beacon_dist)
    beyond_perimeter = beacon_dist + 1
    for row_change in range(0, beyond_perimeter+1):
        col_change = beyond_perimeter - row_change
        for row_mult, col_mult in mult:
            new_row = sensor_row + row_mult * row_change
            new_col = sensor_col + col_mult * col_change
            if new_row >= 0 and new_row <= MAX_ROW and new_col >= 0 and new_col <= MAX_COL:
                points_one_beyond_perimeter[(new_row, new_col)] += 1

# for a point to be a lone empty spot, it needs to be 1 beyond the perimeter of at least 4 sensors' areas
to_check = set()
for k, v in points_one_beyond_perimeter.items():
    if v >= 4:
        to_check.add(k)

# For each of the remaining possibilities, check if there are any sensors that cover its area.
# Stop when we find one that isn't covered by any of the sensors.
for check_row, check_col in to_check:
    eliminated = False
    for ((sensor_row, sensor_col), beacon_dist) in sensor_lst:
        if manhattan_dist(sensor_row, sensor_col, check_row, check_col) <= beacon_dist:
            eliminated = True
            break
    if not eliminated:
        break

print(check_row, check_col)
print(check_col * 4_000_000 + check_row)
