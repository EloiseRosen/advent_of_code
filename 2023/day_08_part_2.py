from itertools import cycle
from math import lcm
from functools import reduce


instructs, network = open('input.txt').read().split('\n\n')

# populate network dict and starts
network_dct = {}
starts = []
network_lines = list(map(lambda x: x.split(' = '), network.split('\n')))
for curr_loc, new_locs in network_lines:
    network_dct[curr_loc] = new_locs[1:-1].split(', ')
    if curr_loc.endswith('A'):
        starts.append(curr_loc)

def get_length(curr):
    c = cycle(instructs)
    length = 0
    while curr[-1] != 'Z':
        curr = network_dct[curr][0 if next(c) == 'L' else 1]
        length += 1
    return length

lengths = [] 
for start in starts:
    lengths.append(get_length(start))

print(reduce(lambda n1, n2: lcm(n1, n2), lengths))
