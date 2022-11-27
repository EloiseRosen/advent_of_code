lst = [int(row) for row in open('input.txt').read().split('\n')]
ans = 0
for idx in range(3, len(lst)):
    if sum(lst[idx-2:idx+1]) > sum(lst[idx-3:idx]):
        ans += 1
print(ans)
