lst = open('input.txt').read().split('\n')

horizontal = 0
depth = 0
for el in lst:
    direction, num = el.split(' ')
    num = int(num)
    if direction == 'forward':
        horizontal += num
    elif direction == 'down':
        depth += num
    elif direction == 'up':
        depth -= num

print(horizontal * depth)
