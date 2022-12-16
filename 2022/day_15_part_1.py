lst = [line.split(': ') for line in open('input.txt').read().split('\n')]
CHECK_ROW = 2_000_000


def manhattan_dist(row1, col1, row2, col2):
    return abs(row1 - row2) + abs(col1 - col2)


must_be_empty_cols = set()
contains_beacon_cols = set()
for sensor, beacon in lst:
    sensor_col, sensor_row = map(int, sensor[len('Sensor at x='):].split(', y='))
    beacon_col, beacon_row = map(int, beacon[len('closest beacon is at x='):].split(', y='))

    if beacon_row == CHECK_ROW:
        contains_beacon_cols.add(beacon_col)

    beacon_dist = manhattan_dist(sensor_row, sensor_col, beacon_row, beacon_col)
    # which spots in CHECK_ROW have a manhattan distance that's <= beacon_dist?
    # abs(sensor_row-CHECK_ROW) + abs(sensor_col-col) <= beacon_dist
    # solve for col:
    # eq 1: col <= sensor_col + (beacon_dist - abs(sensor_row-CHECK_ROW))
    # eq 2: col >= sensor_col - (beacon_dist - abs(sensor_row-CHECK_ROW))
    max_col = sensor_col + (beacon_dist - abs(sensor_row-CHECK_ROW))
    min_col = sensor_col - (beacon_dist - abs(sensor_row-CHECK_ROW))
    for col in range(min_col, max_col+1):
        must_be_empty_cols.add(col)

print(len(must_be_empty_cols-contains_beacon_cols))
