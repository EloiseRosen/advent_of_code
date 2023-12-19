import re
from copy import deepcopy


letters = ['x', 'm', 'a', 's']  # index indicates letter number
workflows_input, _ = open('input.txt').read().split('\n\n')

# populate workflows
workflows_dct = {}
for line in workflows_input.split('\n'):
    bracket = line.index('{')
    label = line[:bracket]
    final_instructs = []
    instructs = line[bracket+1:-1].split(',')
    for instruct in instructs:
        if ':' in instruct:
            condition, outcome = instruct.split(':')
            condition = re.split(r'([><])', condition) # split on > or <. Parens for capture group to keep the > or <
            condition[2] = int(condition[2])
            final_instructs.append(condition + [outcome]) # e.g. ['x', '<', 1416, 'A']
        else:
            final_instructs.append([instruct])
    workflows_dct[label] = final_instructs


def get_accepted_ranges():
    ranges = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]
    accepted = []

    def helper(ranges, ruleset):
        rule = ruleset[0]

        if len(rule) == 1:
            if rule[0] == 'A':
                accepted.append(ranges)
            elif rule[0] != 'R':
                helper(ranges, ruleset=workflows_dct[rule[0]])
        else:
            range_idx = letters.index(rule[0])
            split_value = rule[2]

            if rule[1] == '<':
                range_that_passes_condition = deepcopy(ranges)
                range_that_passes_condition[range_idx] = [ranges[range_idx][0], min(ranges[range_idx][1], split_value-1)]
                if range_that_passes_condition[range_idx][0] <= range_that_passes_condition[range_idx][1]:
                    if rule[3] == 'A':
                        accepted.append(range_that_passes_condition)
                    elif rule[3] != 'R':
                        helper(range_that_passes_condition, workflows_dct[rule[3]])
                range_that_fails_condition = deepcopy(ranges)
                range_that_fails_condition[range_idx] = [max(ranges[range_idx][0], split_value), ranges[range_idx][1]]
                if range_that_fails_condition[range_idx][0] <= range_that_fails_condition[range_idx][1]:
                    helper(range_that_fails_condition, ruleset[1:])

            elif rule[1] == '>':
                range_that_passes_condition = deepcopy(ranges)
                range_that_passes_condition[range_idx] = [max(ranges[range_idx][0], split_value+1), ranges[range_idx][1]]
                if range_that_passes_condition[range_idx][0] <= range_that_passes_condition[range_idx][1]:
                    if rule[3] == 'A':
                        accepted.append(range_that_passes_condition)
                    elif rule[3] != 'R':
                        helper(range_that_passes_condition, workflows_dct[rule[3]])
                range_that_fails_condition = deepcopy(ranges)
                range_that_fails_condition[range_idx] = [ranges[range_idx][0], min(ranges[range_idx][1], split_value)]
                if range_that_fails_condition[range_idx][0] <= range_that_fails_condition[range_idx][1]:
                    helper(range_that_fails_condition, ruleset[1:])

    helper(ranges, ruleset=workflows_dct['in'])
    return accepted

accepted_ranges = get_accepted_ranges()
ans = 0
for accepted_range in accepted_ranges:
    sub_ans = 1
    for start, end in accepted_range:
        sub_ans *= end - start + 1
    ans += sub_ans
print(ans)
