
from json import loads
from functools import cmp_to_key

DIVIDERS = [[[2]], [[6]]]
lst = [line.split('\n') for line in open('input.txt').read().split('\n\n')]


def check_order(left, right):
    """1 correct order, -1 incorrect order, 0 not determined (same value)"""
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        elif left == right:
            return 0
        elif left > right:
            return -1

    elif type(left) == list and type(right) == int:
        return check_order(left, [right])
    elif type(left) == int and type(right) == list:
        return check_order([left], right)

    elif type(left) == list and type(right) == list:
        for idx in range(0, max(len(left), len(right))):
            if idx == len(right):
                return -1
            elif idx == len(left):
                return 1
            outcome = check_order(left[idx], right[idx])
            if outcome != 0:
                return outcome
        return 0


all_packets = DIVIDERS[:]
for pair in lst:
    left, right = map(loads, pair)
    all_packets.append(left)
    all_packets.append(right)

all_packets.sort(key=cmp_to_key(check_order), reverse=True)
print((all_packets.index(DIVIDERS[0])+1) * (all_packets.index(DIVIDERS[1])+1))

