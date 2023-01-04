from collections import Counter

STEPS = 10
template, rules_lst = open('input.txt').read().split('\n\n')
template = list(template)
rules_lst = rules_lst.split('\n')

rules_dct = {}  # pair: letter to insert
for rule in rules_lst:
    pair, to_insert = rule.split(' -> ')
    rules_dct[pair] = to_insert

for step in range(0, STEPS):
    new_lst = []
    for idx in range(0, len(template)-1):
        pair = template[idx] + template[idx+1]
        new_lst.append(pair[0])
        new_lst.append(rules_dct[pair])
    new_lst.append(pair[1])
    template = new_lst

counts = Counter(template).most_common()
print(counts[0][1] - counts[-1][1])
