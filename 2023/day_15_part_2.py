def get_hash(s):
    curr = 0
    for char in s:
        curr = ((curr + ord(char))*17) % 256
    return curr


# note: in Python 3.6 and later, dictionary order is guaranteed to be insertion order
boxes = [{} for _ in range(0, 256)]
steps = open('input.txt').read().replace('\n', '').split(',')
for step in steps:
    if '=' in step:
        label, val = step.split('=')
        box_idx = int(get_hash(label))
        boxes[box_idx][label] = int(val)
    else:
        label, val = step.split('-')
        box_idx = int(get_hash(label))
        box = boxes[box_idx]
        if label in box:
            del box[label]

ans = 0
for box_idx in range(0, len(boxes)):
    slot_num = 1
    for k, v in boxes[box_idx].items():
        power = box_idx + 1
        power *= slot_num
        power *= v
        ans += power
        slot_num += 1
print(ans)
