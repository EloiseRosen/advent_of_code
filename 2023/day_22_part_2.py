def drop_block(cube_set, all_settled_cubes):
    while True: # continue dropping until we hit the ground or a settled cube
        new_cube_set = set()
        for x, y, z in cube_set:
                new_z = z-1
                if new_z == 0 or (x, y, new_z) in all_settled_cubes:
                    new_all_settled_cubes = all_settled_cubes.copy()
                    for cube in cube_set:
                        new_all_settled_cubes.add(cube)
                    return cube_set, new_all_settled_cubes
                else:
                    new_cube_set.add( (x, y, new_z) )
        cube_set = new_cube_set


# parse block endpoints, order block descriptions by height
block_endpoints = []
for line in open('input.txt').read().split('\n'):
    endpoint1, endpoint2 = line.split('~')
    x, y, z = list(map(int, endpoint1.split(',')))
    x2, y2, z2 = list(map(int, endpoint2.split(',')))
    block_endpoints.append( ((x,y,z), (x2,y2,z2)) )
block_endpoints.sort(key=lambda block: (block[0][2], block[1][2]))  # order by height

# parse block descriptions into individual cubes
blocks = [] # each element in the list is a set of the cubes making up that block
for block_endpoint in block_endpoints:
    cube_set = set()
    (x,y,z), (x2,y2,z2) = block_endpoint
    for cube_x in range(x, x2+1):
        cube_set.add( (cube_x, y, z) )
    for cube_y in range(y, y2+1):
        cube_set.add( (x, cube_y, z) )
    for cube_z in range(z, z2+1):
        cube_set.add( (x, y, cube_z) )
    blocks.append(cube_set)
    
# get all cubes in their final resting place
all_settled_cubes = set()
for idx, cube_set in enumerate(blocks, 0): # blocks are already in order from lowest to highest!
    settled_cube_set, all_settled_cubes = drop_block(cube_set, all_settled_cubes)
    blocks[idx] = settled_cube_set

# count how many blocks get moved by each disintegration
ans = 0
for disintegrate_idx, block_to_disintegrate in enumerate(blocks):
    temp_blocks = blocks.copy()
    del temp_blocks[disintegrate_idx]

    new_temp_blocks = []
    # get all cubes in their final resting place
    temp_all_settled_cubes = set()
    for idx, cube_set in enumerate(temp_blocks, 0):
        settled_cube_set, temp_all_settled_cubes = drop_block(cube_set, temp_all_settled_cubes)
        new_temp_blocks.append(settled_cube_set)

    for compare_idx in range(0, len(temp_blocks)):
        if temp_blocks[compare_idx] != new_temp_blocks[compare_idx]:
            ans += 1
print(ans)
