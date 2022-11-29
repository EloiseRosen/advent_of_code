lst = [int(row) for row in open('input.txt').read().split(',')]
min_fuel = None
min_pos = None

for align_pos in range(min(lst), max(lst)+1):
    fuel = 0
    for crab_pos in lst:
        fuel += abs(align_pos - crab_pos)
    if min_fuel is None or fuel < min_fuel:
        min_fuel = fuel
        min_pos = align_pos

print(min_pos)
print(min_fuel)
