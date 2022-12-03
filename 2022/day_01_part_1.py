lst = open('input.txt').read().split('\n\n')

most = 0
for sublst in lst:
    total = sum(map(int, sublst.split('\n')))
    if total > most:
        most = total
print(most)
