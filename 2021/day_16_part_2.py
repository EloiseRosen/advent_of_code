from functools import reduce

binary = ''
for char in open('input.txt').read():
    binary += bin(int(char, 16))[2:].zfill(4)


def process(curr_idx):
    if curr_idx >= len(binary) or int(binary[curr_idx:]) == 0:
        return 0, curr_idx

    version = int(binary[curr_idx:curr_idx+3], 2)
    type_id = int(binary[curr_idx+3:curr_idx+6], 2)
    curr_idx += 6

    if type_id == 4:
        type_4_result = ''
        last_piece = False
        while not last_piece:
            piece = binary[curr_idx:curr_idx+5]
            curr_idx += 5
            last_piece = piece[0] == '0'
            type_4_result += piece[1:]
        return int(type_4_result, 2), curr_idx

    else:  # operator
        length_type_id = binary[curr_idx]
        curr_idx += 1
        assert length_type_id in ['0', '1']
        values = []
        if length_type_id == '0':
            length_of_subpackets = int(binary[curr_idx:curr_idx+15], 2)
            end_idx = curr_idx + 15 + length_of_subpackets
            curr_idx += 15
            while curr_idx < end_idx:
                value, curr_idx = process(curr_idx)
                values.append(value)  
        elif length_type_id == '1':
            num_subpackets = int(binary[curr_idx:curr_idx+11], 2)
            curr_idx += 11
            curr_subpacket = 0
            while curr_subpacket < num_subpackets:
                value, curr_idx = process(curr_idx)     
                values.append(value)
                curr_subpacket += 1

        if type_id == 0:
            rtn_val = sum(values)
        elif type_id == 1:
            rtn_val = reduce(lambda a, b: a * b, values)
        elif type_id == 2:
            rtn_val = min(values)
        elif type_id == 3:
            rtn_val = max(values)
        elif type_id == 5:
            rtn_val = int(values[0] > values[1])
        elif type_id == 6:
            rtn_val = int(values[0] < values[1])
        elif type_id == 7:
            rtn_val = int(values[0] == values[1])
        return rtn_val, curr_idx


value, _ = process(curr_idx=0)
print(value)
