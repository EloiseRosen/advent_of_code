from collections import defaultdict

STEPS = 40

template, rules_lst = open('input.txt').read().split('\n\n')
template = list(template)
rules_lst = rules_lst.split('\n')
rules_dct = {}  # pair: letter to insert
for rule in rules_lst:
    pair, to_insert = rule.split(' -> ')
    rules_dct[pair] = to_insert

count_pairs_dct = defaultdict(lambda: 0)
for idx in range(0, len(template)-1):
    pair = template[idx] + template[idx+1]
    count_pairs_dct[pair] += 1

for step in range(0, STEPS):
    new_count_pairs_dct = defaultdict(lambda: 0)
    for pair, count in count_pairs_dct.items():
        new_letter = rules_dct[pair]
        new_count_pairs_dct[pair[0] + new_letter] += count
        new_count_pairs_dct[new_letter + pair[1]] += count
    count_pairs_dct = new_count_pairs_dct

count_letters_dct = defaultdict(lambda: 0)
for pair, count in count_pairs_dct.items():
    count_letters_dct[pair[0]] += count
count_letters_dct[template[-1]] += 1

largest = None
smallest = None
for count in count_letters_dct.values():
    if largest is None or count > largest:
        largest = count
    if smallest is None or count < smallest:
        smallest = count
print(largest - smallest)
