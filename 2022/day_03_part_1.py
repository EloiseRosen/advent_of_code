from string import ascii_lowercase, ascii_uppercase
score_by_idx = ' ' + ascii_lowercase + ascii_uppercase

lst = open('input.txt').read().split('\n')
ans = 0
for rucksack in lst:
    compartment_1 = set(rucksack[:len(rucksack)//2])
    compartment_2 = set(rucksack[len(rucksack)//2:])
    letter_in_both = next(iter(compartment_1 & compartment_2))
    ans += score_by_idx.index(letter_in_both)
print(ans)
