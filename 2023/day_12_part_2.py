def valid_placement(spring_map, spring_map_idx, block_to_place):
    if spring_map_idx + block_to_place > len(spring_map):
        return False
    if spring_map_idx-1 >= 0 and spring_map[spring_map_idx-1] in '#':
        return False
    for block_idx in range(0, block_to_place-1):
        if spring_map[spring_map_idx+block_idx] not in '#?':
            return False
    if spring_map[spring_map_idx+block_to_place-1] not in '.?':
        return False
    return True


def get_ways(spring_map, spring_counts):
    memo = {}  # {(spring_map_idx, to_place_idx): ways}

    def helper(spring_map_idx, spring_to_place_idx):
        if (spring_map_idx, spring_to_place_idx) in memo:
            return memo[(spring_map_idx, spring_to_place_idx)]
        if spring_to_place_idx > len(spring_counts)-1:
            return 0 if '#' in spring_map[spring_map_idx:] else 1
        if spring_map_idx > len(spring_map)-1:
            return 1 if spring_to_place_idx > len(spring_counts)-1 else 0

        ways = 0
        spring_to_place = spring_counts[spring_to_place_idx]+1 # +1 for trailing period
        for start_idx in range(spring_map_idx, len(spring_map)):
            if valid_placement(spring_map, start_idx, spring_to_place):
                ways += helper(start_idx+spring_to_place, spring_to_place_idx+1)
            if spring_map[start_idx] == '#': # we MUST place here, we can't just skip over this spot
                break
        memo[(spring_map_idx, spring_to_place_idx)] = ways
        return ways
    return helper(spring_map_idx=0, spring_to_place_idx=0)


ans = 0
for line in open('input.txt').read().split('\n'):
    spring_map, spring_counts = line.split(' ')
    spring_map = '?'.join([spring_map]*5) # new in part 2
    spring_map = list(spring_map) + ['.'] # extra period so last grouping always matches
    spring_counts = list(map(int, spring_counts.split(',')))
    spring_counts = spring_counts*5 # new in part 2
    ans += get_ways(spring_map, spring_counts)
print(ans)
