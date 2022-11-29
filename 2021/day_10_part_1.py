lst = open('input.txt').read().split('\n')
pairs_dct = {'(': ')', '[': ']', '{': '}', '<': '>'}
values_dct = {')': 3, ']': 57, '}': 1197, '>': 25137}


def get_syntax_error_score(line):
    stack = []
    for symbol in line:
        if symbol in pairs_dct.keys():  # is an open symbol
            stack.append(symbol)
        else:  # is an close symbol
            if pairs_dct[stack[-1]] != symbol:  # last symbol on stack doesn't match, so line corrupted
                return values_dct[symbol]
            else:
                stack.pop()
    return 0


ans = 0
for line in lst:
    ans += get_syntax_error_score(line)
print(ans)
