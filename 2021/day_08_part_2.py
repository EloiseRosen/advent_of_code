from itertools import permutations

letters = 'abcdefg'
perms = [''.join(p) for p in permutations(letters)]

#  the digit 0 is in index 0, the digit 1 is in index 1, etc.
valid_arrangements = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 
                      'abdefg', 'acf', 'abcdefg', 'abcdfg']


def is_valid(inputs, trans_mapping):
    for input_ in inputs:
        translated_input = input_.translate(trans_mapping)
        translated_input = ''.join(sorted(translated_input))
        if translated_input not in valid_arrangements:
            return False
    return True


def get_decoded_output(inputs, outputs):
    for perm in perms:  # try possible perms until we find one that results in all valid letters
        trans_mapping = str.maketrans(perm, letters)
        if is_valid(inputs, trans_mapping):
            rtn = []
            for output in outputs:
                decoded_letters = output.translate(trans_mapping)
                decoded_letters = ''.join(sorted(decoded_letters))
                rtn.append(str(valid_arrangements.index(decoded_letters)))
            return int(''.join(rtn))


lst = open('input.txt').read().split('\n')
ans = 0
for line in lst:
    inputs, outputs = line.split(' | ')
    inputs = inputs.split(' ')
    outputs = outputs.split(' ')
    ans += get_decoded_output(inputs, outputs)
print(ans)
