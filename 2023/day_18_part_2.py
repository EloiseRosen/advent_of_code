DIRS = ['R', 'D', 'L', 'U']  # index indicates the direction number


instructions = []
for line in open('input.txt').read().split('\n'):
    _, _, code = line.split(' ')
    amount = int(code[2:7], 16)
    dir_ = DIRS[int(code[7])]
    instructions.append( (amount, dir_) )

# these will have contents [length of edge int, y position int]
# then the area of that rectangle is just length of edge * y position
rectangle_to_add = []
rectangle_to_subtact = []

perimeter = 0
y = 0
min_y = float('inf')
for  amount, dir_ in instructions:
    perimeter += amount
    if dir_ == 'U':
        y += amount
    elif dir_ == 'D':
        y -= amount
        min_y = min(y, min_y)
    elif dir_ == 'R':
        rectangle_to_add.append( [amount, y] )
    elif dir_ == 'L':
        rectangle_to_subtact.append( [amount, y] )

# make all ys positive
for idx in range(0, len(rectangle_to_add)):
    rectangle_to_add[idx][1] += abs(min_y)
for idx in range(0, len(rectangle_to_subtact)):
    rectangle_to_subtact[idx][1] += abs(min_y)

area_inside = 0
for edge_length, y in rectangle_to_add:
    area_inside += y * edge_length
for edge_length, y in rectangle_to_subtact:
    area_inside -= y * edge_length

total_area = area_inside + perimeter//2 + 1
print(area_inside + perimeter//2 + 1)
