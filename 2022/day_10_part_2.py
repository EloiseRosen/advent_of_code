instructs = (line for line in open('input.txt').read().split('\n'))
WIDTH = 40
HEIGHT = 6
x = 1
output = []

wait_num = None
for cycle in range(1, WIDTH*HEIGHT+1):
    if cycle%WIDTH-1 in [x-1, x, x+1]:
        output.append('#')
    else:
        output.append('.')

    if wait_num is not None:
        x += wait_num
        wait_num = None
    else:
        instruct = next(instructs)
        if instruct.startswith('addx '):
            _, num = instruct.split(' ')
            wait_num = int(num)

output = ''.join(output)
for mult in range(0, HEIGHT):
    print(output[WIDTH*mult:WIDTH*(mult+1)])
