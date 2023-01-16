from collections import defaultdict

lines = open('input.txt').read().split('\n')
final_dct = defaultdict(lambda: 0)


def get_overlap_cuboid_dims(dims1, dims2):
    for idx in [0, 1, 2]:
        if max(dims1[idx]) < min(dims2[idx]) or min(dims1[idx]) > max(dims2[idx]):
            # print('no overlap', dims1, dims2)
            return None
    rtn = []
    for idx in [0, 1, 2]:
        rtn.append((max(dims1[idx][0], dims2[idx][0]), min(dims1[idx][1], dims2[idx][1])))
    return rtn


for line in lines:
    on_off, dimensions = line.split(' ')
    is_on = 1 if on_off == 'on' else 0
    x_min_max, y_min_max, z_min_max = dimensions.split(',')
    x_min_max = tuple(map(int, x_min_max[2:].split('..')))
    y_min_max = tuple(map(int, y_min_max[2:].split('..')))
    z_min_max = tuple(map(int, z_min_max[2:].split('..')))
    dims = (x_min_max, y_min_max, z_min_max)

    new_cuboid_dct = defaultdict(lambda: 0)
    for existing_cuboid in final_dct:
        # remove intersecitons with previous cubes so we're not double counting
        overlap_cuboid_dims = get_overlap_cuboid_dims(dims, existing_cuboid)
        if overlap_cuboid_dims:
            new_cuboid_dct[tuple(overlap_cuboid_dims)] -= final_dct[existing_cuboid]

    # turn on the new cuboid area if applicable
    if is_on:
        new_cuboid_dct[dims] += 1

    for dims in new_cuboid_dct:
        final_dct[dims] += new_cuboid_dct[dims]

ans = 0
for dims, contribution in final_dct.items():
    volume = (abs(dims[0][1]-dims[0][0])+1) * (abs(dims[1][1]-dims[1][0])+1) * (abs(dims[2][1]-dims[2][0])+1)
    ans += volume * contribution
print(ans)
