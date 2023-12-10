lines = open('input.txt').read().split('\n')

ans = 0
for line in lines:
    lst = list(map(lambda x: int(x), line.split(' ')))
    lst = lst[::-1]  # for part 2, reverse list
    lsts = [lst]
    while not all([num == 0 for num in lsts[-1]]):
        last_lst = lsts[-1]
        new_lst = []
        for idx in range(0, len(last_lst)-1):
            new_lst.append(last_lst[idx+1] - last_lst[idx])
        lsts.append(new_lst)
    lsts[-1].append(0)
    for lst_idx in range(len(lsts)-1, 0, -1):
        new_val = lsts[lst_idx][-1] + lsts[lst_idx-1][-1]
        lsts[lst_idx-1].append(new_val)
    ans += lsts[0][-1]

print(ans)
