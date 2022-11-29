lst = open('input.txt').read().split('\n')
ans = 0
for line in lst:
    _, outputs = line.split(' | ')
    outputs = outputs.split(' ')
    for output in outputs:
        if len(output) in [2, 3, 4, 7]:
            ans += 1

print(ans)
