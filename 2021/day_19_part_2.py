from itertools import permutations, product


POINT_MATCH_REQ = 12
# with 12 points, the first is paired with all other 11 points, then then second
# has 10 points left to be paired with, etc.  11+10+9+8+... -> Triangle numbers!
# n * (n+1) / 2 where n is 1 less than MATCH_REQ
comparison_match_req = ((POINT_MATCH_REQ-1) * (POINT_MATCH_REQ-1+1)) / 2

# We could be switching around coordinates (e.g. the y becomes the z) as well as signs (pos becomes neg).
# POSSIBLE_ROTATIONS is all the sign and switched coordinate changes that could be made.
POSSIBLE_ROTATIONS = []
for sign1, sign2, sign3 in product([-1, 1], repeat=3):
    for coord_idx_1, coord_idx_2, coord_idx_3 in permutations([0, 1, 2]):
        POSSIBLE_ROTATIONS.append(((sign1, coord_idx_1), (sign2, coord_idx_2), (sign3, coord_idx_3)))

TEST_POINT = (3, 2, 1)

lst = [row.split('\n') for row in open('input.txt').read().split('\n\n')]
scanner_to_points_dct = {}  # scanner id: list of points as tuples
for scanner in lst:
    key = int(scanner[0][len('--- scanner '):-4])
    sublst = []
    for point in scanner[1:]:
        sublst.append(tuple(map(int, point.split(','))))
    scanner_to_points_dct[key] = sublst


def get_rotations(point):
    rtn = []
    for (sign1, coord_idx_1), (sign2, coord_idx_2), (sign3, coord_idx_3) in POSSIBLE_ROTATIONS:
        rtn.append((sign1*point[coord_idx_1], sign2*point[coord_idx_2], sign3*point[coord_idx_3]))
    return rtn


def abs_val_changes_between_points(points):
    changes = set()
    for idx1 in range(0, len(points)):
        for idx2 in range(idx1+1, len(points)):
            point1 = points[idx1]
            point2 = points[idx2]
            changes.add(tuple(sorted((abs(point1[0]-point2[0]), 
                                        abs(point1[1]-point2[1]), 
                                        abs(point1[2]-point2[2])))))
    return changes


def get_successful_rotation_and_offset(scanner_1_points, scanner_2_points):
    for scanner_1_idx_1 in range(0, len(scanner_1_points)):
        for scanner_1_idx_2 in range(scanner_1_idx_1+1, len(scanner_1_points)):
            for scanner_2_idx_1 in range(0, len(scanner_2_points)):
                for scanner_2_idx_2 in range(scanner_2_idx_1+1, len(scanner_2_points)):
                    anchor_point = scanner_1_points[scanner_1_idx_1]
                    dx_dy_dz_scanner_1_pair = (scanner_1_points[scanner_1_idx_1][0] - scanner_1_points[scanner_1_idx_2][0], 
                                               scanner_1_points[scanner_1_idx_1][1] - scanner_1_points[scanner_1_idx_2][1], 
                                               scanner_1_points[scanner_1_idx_1][2] - scanner_1_points[scanner_1_idx_2][2])
                    dx_dy_dz_scanner_2_pair = (scanner_2_points[scanner_2_idx_1][0] - scanner_2_points[scanner_2_idx_2][0], 
                                               scanner_2_points[scanner_2_idx_1][1] - scanner_2_points[scanner_2_idx_2][1], 
                                               scanner_2_points[scanner_2_idx_1][2] - scanner_2_points[scanner_2_idx_2][2])

                    rotated_offsets_options = []  # need to try both pos and neg, so there are 2 options
                    rotated_offsets_options.append(get_rotations(dx_dy_dz_scanner_2_pair))
                    rotated_offsets_options.append(get_rotations((-dx_dy_dz_scanner_2_pair[0],
                                                                  -dx_dy_dz_scanner_2_pair[1], 
                                                                  -dx_dy_dz_scanner_2_pair[2])))
                    for rotated_offsets in rotated_offsets_options:
                        for rotation_idx in range(0, len(rotated_offsets)):
                            if rotated_offsets[rotation_idx] == dx_dy_dz_scanner_1_pair:  # this rotation gives the right changes

                                # for our set of points, get the e.g. -x, z, y version of those points
                                post_rotation_scanner_2_points = []
                                for scanner_2_point in scanner_2_points:
                                    post_rotation_scanner_2_points.append(get_rotations(scanner_2_point)[rotation_idx])

                                # also apply offset
                                for post_rotation_scanner_2_point in post_rotation_scanner_2_points:
                                    offset_x, offset_y, offset_z = (anchor_point[0] - post_rotation_scanner_2_point[0], 
                                                                    anchor_point[1] - post_rotation_scanner_2_point[1], 
                                                                    anchor_point[2] - post_rotation_scanner_2_point[2])
                                    post_offset_scanner_2_points  = []
                                    for post_rotation_scanner_2_point in post_rotation_scanner_2_points:
                                        post_offset_scanner_2_points.append((post_rotation_scanner_2_point[0] + offset_x, 
                                                                            post_rotation_scanner_2_point[1] + offset_y, 
                                                                            post_rotation_scanner_2_point[2] + offset_z))

                                    if len(set(scanner_1_points) & set(post_offset_scanner_2_points)) >= POINT_MATCH_REQ:
                                        return rotation_idx, (offset_x, offset_y, offset_z)
    return None, None


def get_opposite_rotation_idx(original_rotation_idx):
    original = get_rotations(TEST_POINT)[original_rotation_idx]
    for rotation_idx in range(0, len(POSSIBLE_ROTATIONS)):
        if get_rotations(original)[rotation_idx] == TEST_POINT:
            return rotation_idx


def new_rotation_idx(rotation_idx_1, rotation_idx_2):
    one = get_rotations(TEST_POINT)[rotation_idx_1]
    two = get_rotations(one)[rotation_idx_2]
    for rotation_idx in range(0, len(POSSIBLE_ROTATIONS)):
        if get_rotations(TEST_POINT)[rotation_idx] == two:
            return rotation_idx


scanner_to_point_changes_dct = {}
for scanner, points in scanner_to_points_dct.items():
    scanner_to_point_changes_dct[scanner] = abs_val_changes_between_points(points)

could_have_overlap = []
for scanner1 in range(0, len(scanner_to_point_changes_dct)):
    for scanner2 in range(scanner1+1, len(scanner_to_point_changes_dct)):
        point_changes_1_set = scanner_to_point_changes_dct[scanner1]
        point_changes_2_set = scanner_to_point_changes_dct[scanner2]
        if len(point_changes_1_set & point_changes_2_set) >= comparison_match_req:
            could_have_overlap.append({scanner1, scanner2})

rotation_and_offset_between_scanners = {}  # scanner 1: [[scanner 2, rotation, offset], [scanner 3, rotation, offset]]
for scanner_1, scanner_2 in could_have_overlap: 
    rotation, offset = get_successful_rotation_and_offset(scanner_to_points_dct[scanner_1], scanner_to_points_dct[scanner_2])
    if rotation is not None and offset is not None:
        if scanner_1 in rotation_and_offset_between_scanners:
            rotation_and_offset_between_scanners[scanner_1].append([scanner_2, rotation, offset])
        else:
            rotation_and_offset_between_scanners[scanner_1] = [[scanner_2, rotation, offset]]

        scanner_2_rotation = get_opposite_rotation_idx(rotation)
        scanner_2_offset = get_rotations((-offset[0], -offset[1], -offset[2]))[get_opposite_rotation_idx(rotation)]
        if scanner_2 in rotation_and_offset_between_scanners:
            rotation_and_offset_between_scanners[scanner_2].append([scanner_1, scanner_2_rotation, scanner_2_offset])
        else:
            rotation_and_offset_between_scanners[scanner_2] = [[scanner_1, scanner_2_rotation, scanner_2_offset]]

stack = [[0, 0, (0, 0, 0)]]  # scanner, rotation, offset
seen = set()
final_unique_points = set()
part2 = []
while stack:
    scanner, rotation, offset = stack.pop()
    if scanner not in seen:
        part2.append(offset)
        seen.add(scanner)
        for point in scanner_to_points_dct[scanner]:
            post_rotation = get_rotations(point)[rotation]
            post_offset = (post_rotation[0] + offset[0],
                           post_rotation[1] + offset[1],
                           post_rotation[2] + offset[2])
            final_unique_points.add(post_offset)

        for new_scanner, new_rotation, new_offset in rotation_and_offset_between_scanners[scanner]:
            if new_scanner not in seen:
                new_rotation = new_rotation_idx(new_rotation, rotation)
                offset_change = get_rotations(new_offset)[rotation]
                new_offset = [offset[0] + offset_change[0],
                               offset[1] + offset_change[1],
                               offset[2] + offset_change[2]]
                stack.append([new_scanner, new_rotation, new_offset])

max_dist = None
for idx1 in range(0, len(part2)):
    for idx2 in range(idx1+1, len(part2)):
        point1 = part2[idx1]
        point2 = part2[idx2]
        new_dist = abs(point1[0]-point2[0]) + abs(point1[1]-point2[1]) + abs(point1[2]-point2[2])
        if max_dist is None or new_dist > max_dist:
            max_dist = new_dist
print(max_dist)
