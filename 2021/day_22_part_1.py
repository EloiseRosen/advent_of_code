lines = open('input.txt').read().split('\n')
LOWER_BOUND = -50
UPPER_BOUND = 50
dct = {}  # (x, y, z): is_on

for line in lines:
    on_off, dimensions = line.split(' ')
    x_min_max, y_min_max, z_min_max = dimensions.split(',')
    x_min_max = tuple(map(int, x_min_max[2:].split('..')))
    y_min_max = tuple(map(int, y_min_max[2:].split('..')))
    z_min_max = tuple(map(int, z_min_max[2:].split('..')))
    for x in range(max(x_min_max[0], LOWER_BOUND), min(x_min_max[1], UPPER_BOUND)+1):
        for y in range(max(y_min_max[0], LOWER_BOUND), min(y_min_max[1], UPPER_BOUND)+1):
            for z in range(max(z_min_max[0], LOWER_BOUND), min(z_min_max[1], UPPER_BOUND)+1):
                dct[(x, y, z)] = 1 if on_off == 'on' else 0

print(sum(is_on for is_on in dct.values()))
