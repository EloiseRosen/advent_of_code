lst = open('input.txt').read().split('\n')

horizontal = 0
depth = 0
aim = 0
for el in lst:
    direction, num = el.split(' ')
    num = int(num)
    if direction == 'forward':
        horizontal += num
        depth += aim * num
    elif direction == 'down':
        aim += num
    elif direction == 'up':
        aim -= num

print(horizontal * depth)
