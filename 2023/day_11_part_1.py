from itertools import combinations


GROWTH_SIZE = 2

# read in
grid = [r for r in open('input.txt').read().split('\n')]

# determine galaxy locations and empty rows and cols
empty_rows = {r for r in range(0, len(grid))}
empty_cols = {c for c in range(0, len(grid[0]))}
galaxies = set()
for r in range(0, len(grid)):
    for c in range(0, len(grid[0])):
        if grid[r][c] == '#':
            galaxies.add( (r, c) )
            empty_rows.discard(r)
            empty_cols.discard(c)

# populate the expansion indicies
row_offset = [0 if r not in empty_rows else (GROWTH_SIZE-1) for r in range(0, len(grid))]
col_offset = [0 if c not in empty_cols else (GROWTH_SIZE-1) for c in range(0, len(grid[0]))]

# turn expansion indicies into cumulative sum
for idx in range(1, len(row_offset)):
    row_offset[idx] = row_offset[idx] + row_offset[idx-1] 
for idx in range(1, len(col_offset)):
    col_offset[idx] = col_offset[idx] + col_offset[idx-1]

# apply offsets to galaxies
offset_galaxies = set()
for galaxy_r, galaxy_c in galaxies:
    offset_galaxy_r = galaxy_r + row_offset[galaxy_r]
    offset_galaxy_c = galaxy_c + col_offset[galaxy_c]
    offset_galaxies.add( (offset_galaxy_r, offset_galaxy_c) )

# get sum of manhattan distances
ans = 0
for point1, point2 in combinations(offset_galaxies, 2):
    ans += abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])  # manhattan distance
print(ans)
