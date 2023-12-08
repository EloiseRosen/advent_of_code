from itertools import cycle


START, END = 'AAA', 'ZZZ'
instructs, network = open('input.txt').read().split('\n\n')
c = cycle(instructs)

# populate network dict
network_dct = {}
network_lines = list(map(lambda x: x.split(' = '), network.split('\n')))
for curr_loc, new_locs in network_lines:
    network_dct[curr_loc] = new_locs[1:-1].split(', ')

steps = 0
curr = START
while curr != END:
    instruct = next(c)
    curr = network_dct[curr][0 if instruct == 'L' else 1]
    steps += 1


print(steps)
