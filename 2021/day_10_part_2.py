lst = open('input.txt').read().split('\n')
pairs_dct = {'(': ')', '[': ']', '{': '}', '<': '>'}
values_dct = {'(': 1, '[': 2, '{': 3, '<': 4}


def get_closing_sequence_score(line):
    stack = []
    for symbol in line:
        if symbol in pairs_dct.keys():  # is an open symbol
            stack.append(symbol)
        else:  # is a close symbol
            if pairs_dct[stack[-1]] != symbol:  # corrupted line, so no closing sequence score
                return None
            else:
                stack.pop()
    score = 0
    for idx in range(len(stack)-1, -1, -1):
        score *= 5
        score += values_dct[stack[idx]]
    return score


scores = []
for line in lst:
    score = get_closing_sequence_score(line)
    if score is not None:
        scores.append(score)

scores.sort()
print(scores[len(scores)//2])
