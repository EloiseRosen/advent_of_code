
KEY = 811589153
TIMES = 10
lst = [(idx, int(row)*KEY) for idx, row in enumerate(open('input.txt').read().split('\n'))]  # (item_id, val)

for _ in range(0, TIMES):
    for item_id in range(0, len(lst)):
        # find the item we need to move this time
        for idx in range(0, len(lst)):
            tup = lst[idx]
            if tup[0] == item_id:
                break

        # put it in its new position
        if tup[1] != 0:
            lst.pop(idx)
            new_idx = idx + tup[1]
            new_idx = new_idx % len(lst)
            if new_idx < 0:
                new_idx += len(lst)
            lst.insert(new_idx, tup)
            
    for idx, tup in enumerate(lst):
        if tup[1] == 0:
            zero_idx = idx
            break
print(lst[(zero_idx+1000)%len(lst)][1] + lst[(zero_idx+2000)%len(lst)][1] + lst[(zero_idx+3000)%len(lst)][1])
