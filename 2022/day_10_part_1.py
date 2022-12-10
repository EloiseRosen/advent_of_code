instructs = (line for line in open('input.txt').read().split('\n'))
x = 1
checkpoints = [20+mult*40 for mult in range(0, 6)]
ans = 0

wait_num = None
for cycle in range(1, checkpoints[-1]+1):
    if cycle in checkpoints:
        ans += cycle * x

    if wait_num is not None:
        x += wait_num
        wait_num = None
    else:
        instruct = next(instructs)
        if instruct.startswith('addx '):
            _, num = instruct.split(' ')
            wait_num = int(num)
    
print(ans)
