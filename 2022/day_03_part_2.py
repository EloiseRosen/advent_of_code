from string import ascii_lowercase, ascii_uppercase
score_by_idx = ' ' + ascii_lowercase + ascii_uppercase

lst = open('input.txt').read().split('\n')
ans = 0
for idx in range(0, len(lst), 3):
    letter_in_all = next(iter(set(lst[idx]) & set(lst[idx+1]) & set(lst[idx+2])))
    ans += score_by_idx.index(letter_in_all)
print(ans)
