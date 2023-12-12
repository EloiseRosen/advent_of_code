from itertools import groupby


def generate_unique_perms(symbol_dct):
    """Generate permutations without generating any duplicates."""
    if len(symbol_dct) == 1:
        char, cnt = next(iter(symbol_dct.items()))
        return [[char] * cnt]
    rtn = []
    # can start with each of the unique letters
    for char, cnt in symbol_dct.items():
        start = char
        dct_copy = symbol_dct.copy()
        dct_copy[char] -= 1
        if dct_copy[char] == 0:
            del dct_copy[char]
        rest = generate_unique_perms(dct_copy)
        for way in rest:
            rtn.append([start] + way)
    return rtn


def is_valid(spring_map, spring_counts):
    """Returns whether this spring_map matches spring_counts."""
    new_spring_counts = []
    for char, group in groupby(spring_map):
        if char == '#':
            new_spring_counts.append(len(list(group)))
    return new_spring_counts == spring_counts


def ways(spring_map, spring_counts):
    """Returns number of ways #s can be placed in `spring_map` to match `spring_counts`."""
    # generate the unique permutations
    num_missing_hash = sum(spring_counts) - spring_map.count('#')
    num_q = spring_map.count('?')
    symbol_dct = {}
    if num_missing_hash > 0:
        symbol_dct['#'] = num_missing_hash
    if num_q-num_missing_hash > 0:
        symbol_dct['.'] = num_q-num_missing_hash
    unique_perms = generate_unique_perms(symbol_dct)

    # count valid ways
    ways = 0
    for unique_perm in unique_perms:
        # construct the spring map for this permutation
        it = iter(unique_perm)
        new_spring_map = []
        for el in spring_map:
            if el == '?':
                new_spring_map.append(next(it))
            else:
                new_spring_map.append(el)

        if is_valid(new_spring_map, spring_counts):
            ways += 1
    return ways


ans = 0
for line in open('input.txt').read().split('\n'):
    spring_map, spring_counts = line.split(' ')
    spring_map = list(spring_map)
    spring_counts = list(map(int, spring_counts.split(',')))
    ans += ways(spring_map, spring_counts)
print(ans)
