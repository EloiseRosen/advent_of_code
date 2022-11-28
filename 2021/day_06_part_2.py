from collections import Counter

DAYS = 256
lst = [int(row) for row in open('input.txt').read().split(',')]
dct = Counter(lst)

for day in range(0, DAYS):
    for key in range(0, 9):
        dct[key-1] = dct[key]
    dct[8] = dct[-1]  # new babies
    dct[6] += dct[-1]  # back to start of cycle
    dct[-1] = 0

ans = 0
for count in dct.values():
    ans += count
print(ans)
