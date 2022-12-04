lst = [line.split(',') for line in open('input.txt').read().split('\n')]
overlaps = 0
for range_1, range_2 in lst:
    range_1_start, range_1_end =  map(int, range_1.split('-'))
    range_2_start, range_2_end =  map(int, range_2.split('-'))
    if ((range_1_end >= range_2_start and range_1_end <= range_2_end) or 
    (range_2_end >= range_1_start and range_2_end <= range_1_end)):
        overlaps += 1
print(overlaps)
