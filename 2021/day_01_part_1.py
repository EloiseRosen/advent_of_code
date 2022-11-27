lst = [int(row) for row in open('input.txt').read().split('\n')]
ans = 0
for idx in range(1, len(lst)):
    if lst[idx] > lst[idx-1]:
        ans += 1
print(ans)
